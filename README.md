# ASL Translator - Python Mobile App 🤟

A real-time American Sign Language (ASL) translator mobile app built entirely in **Python** using **Kivy** framework and **Google Gemini Vision API**.

## Features ✨

- 📸 **Real-time Recognition** - Continuously captures and recognizes ASL signs
- 🔤 **Letters & Words** - Recognizes both fingerspelling (A-Z) and word signs
- 🔊 **Text-to-Speech** - Speaks out recognized signs automatically
- 📝 **History Tracking** - Keeps track of last 20 recognized signs
- 🎨 **Beautiful UI** - Modern, dark-themed interface built with Kivy
- 📱 **Cross-platform** - Works on Android, iOS, Windows, Mac, Linux

## Tech Stack 🛠️

- **Python 3.8+**
- **Kivy** - Cross-platform Python framework for mobile apps
- **Google Gemini 2.0 Flash** - Multimodal AI for vision recognition
- **Pillow** - Image processing
- **pyttsx3** - Text-to-speech
- **Buildozer** - Build tool for Android/iOS

## Prerequisites 📋

### For Desktop Testing:
- Python 3.8 or higher
- pip (Python package manager)
- Gemini API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### For Android Build:
- Linux or macOS (Windows users: use WSL2)
- Buildozer dependencies
- Android SDK & NDK

### For iOS Build:
- macOS only
- Xcode
- kivy-ios toolchain

## Installation 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/aiml34048/asl-translator-python.git
cd asl-translator-python
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Open `main.py` and replace line 27:

```python
self.gemini_api_key = "YOUR_GEMINI_API_KEY_HERE"
```

With your actual API key:

```python
self.gemini_api_key = "AIzaSyC...your-actual-key"
```

### 5. Run on Desktop (for testing)

```bash
python main.py
```

## Building for Mobile 📱

### Android Build

#### Install Buildozer Dependencies (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

#### Build APK:

```bash
# Initialize buildozer (first time only)
buildozer init

# Build debug APK
buildozer -v android debug

# Build and deploy to connected device
buildozer android debug deploy run
```

The APK will be in `bin/` folder.

### iOS Build (macOS only)

```bash
# Install kivy-ios
pip install kivy-ios

# Create Xcode project
toolchain build kivy pillow

# Create your app
toolchain create ASLTranslator .

# Open in Xcode
open ASLTranslator-ios/ASLTranslator.xcodeproj
```

## Usage 📱

### Desktop Testing:
1. Run `python main.py`
2. Allow camera access
3. Click "Start Recognition"
4. Show ASL signs to your webcam

### Mobile App:
1. Install the APK on your Android device
2. Grant camera and microphone permissions
3. Tap "Start Recognition"
4. Show ASL signs to the front camera
5. View recognized signs with speech output

## Project Structure 📁

```
asl-translator-python/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── buildozer.spec      # Android/iOS build configuration
├── README.md           # This file
└── bin/                # Built APK files (after build)
```

## Configuration ⚙️

### Change Recognition Interval

In `main.py`, line 127:

```python
self.recognition_event = Clock.schedule_interval(self.capture_and_recognize, 2)
# Change 2 to desired seconds (e.g., 1 for faster, 3 for slower)
```

### Change Camera (Front/Back)

In `main.py`, line 52:

```python
index=1  # 1 = front camera, 0 = back camera
```

### Adjust Image Quality

In `main.py`, line 157:

```python
img.save(img_byte_arr, format='JPEG', quality=70)
# Increase quality (0-100) for better recognition, decrease for faster processing
```

## How It Works 🔍

1. **Camera Capture** - Kivy Camera widget captures live video feed
2. **Frame Processing** - Frames captured every 2 seconds
3. **Image Conversion** - Texture converted to PIL Image, resized and compressed
4. **AI Recognition** - Gemini Vision API analyzes the image
5. **Output** - Recognized text displayed and spoken via TTS
6. **History** - All recognized signs logged with timestamps

## Troubleshooting 🔧

### Camera Not Working (Desktop)
```bash
# Check available cameras
python -c "from kivy.core.camera import Camera; print(Camera.get_cameras())"
```

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Buildozer Errors
```bash
# Clean build
buildozer android clean

# Update buildozer
pip install --upgrade buildozer
```

### API Errors
- Verify Gemini API key is correct
- Check internet connection
- Ensure API quota not exceeded at [Google AI Studio](https://makersuite.google.com/)

### Permission Errors (Android)
- Manually grant Camera and Microphone permissions in Settings > Apps > ASL Translator

## Performance Tips 💡

- **Good lighting** improves recognition accuracy
- **Clear hand positioning** in camera frame
- **Stable hand gestures** for 1-2 seconds
- **Reduce recognition interval** if device is slow
- **Lower image quality** for faster processing on older devices

## Development 🛠️

### Running in Debug Mode

```python
# Add at top of main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testing Without Camera

Replace camera capture with static images for testing:

```python
# In _process_frame method
img = Image.open('test_sign.jpg')
```

## Future Enhancements 🚀

- [ ] Offline mode with TensorFlow Lite
- [ ] Support for more sign languages (BSL, ISL, etc.)
- [ ] Sentence formation from multiple signs
- [ ] Custom sign training
- [ ] Video recording and playback
- [ ] Multi-hand recognition
- [ ] Learning mode with tutorials

## Known Limitations ⚠️

- Requires internet connection for Gemini API
- Recognition accuracy depends on lighting and hand positioning
- Front camera quality affects results
- API rate limits apply (check Google AI Studio)

## Contributing 🤝

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Support 💬

For issues and questions:
- Open an issue on GitHub
- Email: aiml34048@gmail.com

## Acknowledgments 🙏

- Google Gemini AI for powerful vision recognition
- Kivy team for excellent Python mobile framework
- ASL community for inspiration

---

**Made with ❤️ and Python for the deaf and hard-of-hearing community**

## Quick Start Commands 🚀

```bash
# Clone and setup
git clone https://github.com/aiml34048/asl-translator-python.git
cd asl-translator-python
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Add your API key to main.py
# Then run
python main.py

# Build for Android
buildozer android debug
```

Enjoy translating ASL! 🤟
