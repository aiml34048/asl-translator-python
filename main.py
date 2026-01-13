"""
ASL Translator - Real-time Sign Language Recognition
Built with Kivy and Google Gemini Vision API
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
import google.generativeai as genai
from PIL import Image
import io
import base64
from datetime import datetime
import threading
import pyttsx3

# Configure window
Window.clearcolor = (0.1, 0.1, 0.18, 1)

class ASLTranslatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_recognizing = False
        self.gemini_api_key = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your API key
        self.recognition_history = []
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        # Initialize Gemini
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
    def build(self):
        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.15, orientation='vertical')
        title = Label(
            text='ASL Translator',
            font_size='24sp',
            bold=True,
            size_hint_y=0.6
        )
        subtitle = Label(
            text='Real-time Sign Language Recognition',
            font_size='14sp',
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=0.4
        )
        header.add_widget(title)
        header.add_widget(subtitle)
        
        # Camera
        self.camera = Camera(
            resolution=(640, 480),
            size_hint_y=0.35,
            play=True,
            index=1  # Front camera (0 for back camera)
        )
        
        # Result display
        result_layout = BoxLayout(
            size_hint_y=0.15,
            padding=10,
            orientation='vertical'
        )
        result_label = Label(
            text='Recognized:',
            font_size='14sp',
            size_hint_y=0.3,
            color=(0.7, 0.7, 0.7, 1)
        )
        self.result_text = Label(
            text='Show an ASL sign...',
            font_size='28sp',
            bold=True,
            size_hint_y=0.7,
            color=(0.3, 0.8, 0.64, 1)
        )
        result_layout.add_widget(result_label)
        result_layout.add_widget(self.result_text)
        
        # Control buttons
        button_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        self.start_button = Button(
            text='Start Recognition',
            background_color=(0.3, 0.8, 0.64, 1),
            font_size='16sp',
            bold=True
        )
        self.start_button.bind(on_press=self.toggle_recognition)
        button_layout.add_widget(self.start_button)
        
        # History section
        history_header = BoxLayout(size_hint_y=0.05)
        history_title = Label(
            text='History',
            font_size='16sp',
            bold=True,
            halign='left',
            size_hint_x=0.7
        )
        self.clear_button = Button(
            text='Clear',
            size_hint_x=0.3,
            background_color=(0.9, 0.3, 0.24, 1)
        )
        self.clear_button.bind(on_press=self.clear_history)
        history_header.add_widget(history_title)
        history_header.add_widget(self.clear_button)
        
        # History scroll view
        self.history_scroll = ScrollView(size_hint_y=0.2)
        self.history_layout = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None,
            padding=5
        )
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))
        self.history_scroll.add_widget(self.history_layout)
        
        # Add all widgets to main layout
        self.main_layout.add_widget(header)
        self.main_layout.add_widget(self.camera)
        self.main_layout.add_widget(result_layout)
        self.main_layout.add_widget(button_layout)
        self.main_layout.add_widget(history_header)
        self.main_layout.add_widget(self.history_scroll)
        
        return self.main_layout
    
    def toggle_recognition(self, instance):
        if not self.is_recognizing:
            self.start_recognition()
        else:
            self.stop_recognition()
    
    def start_recognition(self):
        self.is_recognizing = True
        self.start_button.text = 'Stop Recognition'
        self.start_button.background_color = (0.9, 0.3, 0.24, 1)
        self.result_text.text = 'Recognizing...'
        
        # Schedule recognition every 2 seconds
        self.recognition_event = Clock.schedule_interval(self.capture_and_recognize, 2)
    
    def stop_recognition(self):
        self.is_recognizing = False
        self.start_button.text = 'Start Recognition'
        self.start_button.background_color = (0.3, 0.8, 0.64, 1)
        
        if hasattr(self, 'recognition_event'):
            self.recognition_event.cancel()
    
    def capture_and_recognize(self, dt):
        """Capture camera frame and send to Gemini for recognition"""
        if not self.camera.texture:
            return
        
        # Run in separate thread to avoid blocking UI
        thread = threading.Thread(target=self._process_frame)
        thread.daemon = True
        thread.start()
    
    def _process_frame(self):
        try:
            # Get camera texture
            texture = self.camera.texture
            if not texture:
                return
            
            # Convert texture to PIL Image
            size = texture.size
            pixels = texture.pixels
            
            # Create PIL Image from texture data
            img = Image.frombytes('RGBA', size, pixels)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip vertically
            img = img.convert('RGB')
            
            # Resize for faster processing
            img.thumbnail((800, 800))
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG', quality=70)
            img_byte_arr = img_byte_arr.getvalue()
            
            # Send to Gemini
            prompt = """You are an ASL (American Sign Language) recognition expert. 
Analyze this image and identify the ASL sign being shown. 
- If it's a letter (fingerspelling), return just the letter (A-Z)
- If it's a word/phrase sign, return the word or phrase
- If no clear ASL sign is detected, return "No sign detected"
- Be concise, return ONLY the recognized sign, nothing else."""
            
            # Create image part for Gemini
            image_part = {
                "mime_type": "image/jpeg",
                "data": img_byte_arr
            }
            
            # Generate response
            response = self.model.generate_content([prompt, image_part])
            recognized_text = response.text.strip()
            
            # Update UI on main thread
            if recognized_text and recognized_text != "No sign detected":
                Clock.schedule_once(lambda dt: self.update_result(recognized_text), 0)
                
        except Exception as e:
            print(f"Recognition error: {e}")
            Clock.schedule_once(lambda dt: self.show_error(), 0)
    
    def update_result(self, text):
        """Update the result display and add to history"""
        self.result_text.text = text
        
        # Add to history
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.add_to_history(text, timestamp)
        
        # Speak the result
        self.speak_text(text)
    
    def speak_text(self, text):
        """Text-to-speech output"""
        try:
            thread = threading.Thread(target=lambda: self.tts_engine.say(text) or self.tts_engine.runAndWait())
            thread.daemon = True
            thread.start()
        except Exception as e:
            print(f"TTS error: {e}")
    
    def add_to_history(self, text, timestamp):
        """Add recognized sign to history"""
        history_item = BoxLayout(
            size_hint_y=None,
            height=40,
            padding=5
        )
        
        text_label = Label(
            text=text,
            font_size='16sp',
            bold=True,
            color=(0.3, 0.8, 0.64, 1),
            halign='left',
            size_hint_x=0.7
        )
        text_label.bind(size=text_label.setter('text_size'))
        
        time_label = Label(
            text=timestamp,
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1),
            halign='right',
            size_hint_x=0.3
        )
        time_label.bind(size=time_label.setter('text_size'))
        
        history_item.add_widget(text_label)
        history_item.add_widget(time_label)
        
        # Add to top of history
        self.history_layout.add_widget(history_item, index=len(self.history_layout.children))
        
        # Keep only last 20 items
        if len(self.history_layout.children) > 20:
            self.history_layout.remove_widget(self.history_layout.children[0])
    
    def clear_history(self, instance):
        """Clear all history items"""
        self.history_layout.clear_widgets()
        self.result_text.text = 'Show an ASL sign...'
    
    def show_error(self):
        """Show error message"""
        self.result_text.text = 'Recognition failed. Try again.'
    
    def on_stop(self):
        """Cleanup when app closes"""
        if self.is_recognizing:
            self.stop_recognition()
        self.camera.play = False

if __name__ == '__main__':
    ASLTranslatorApp().run()
