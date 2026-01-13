# Complete Setup Guide for VS Code 🚀

This guide will walk you through setting up the ASL Translator Python app in VS Code from scratch.

## Prerequisites ✅

Before starting, ensure you have:
- Python 3.8 or higher installed
- VS Code installed
- Git installed
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Step-by-Step Setup 📝

### 1. Open VS Code

Launch Visual Studio Code on your computer.

### 2. Open Terminal in VS Code

Press `` Ctrl+` `` (backtick) or go to `View > Terminal`

### 3. Clone the Repository

In the terminal, run:

```bash
git clone https://github.com/aiml34048/asl-translator-python.git
cd asl-translator-python
```

### 4. Open Project in VS Code

```bash
code .
```

Or: `File > Open Folder` → Select `asl-translator-python`

### 5. Create Virtual Environment

In VS Code terminal:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal.

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Kivy (UI framework)
- google-generativeai (Gemini API)
- Pillow (image processing)
- pyttsx3 (text-to-speech)
- buildozer (for mobile builds)

### 7. Get Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIzaSy...`)

### 8. Add API Key to Code

1. Open `main.py` in VS Code
2. Find line 27:
   ```python
   self.gemini_api_key = "YOUR_GEMINI_API_KEY_HERE"
   ```
3. Replace with your actual key:
   ```python
   self.gemini_api_key = "AIzaSyC...your-actual-key"
   ```
4. Save the file (`Ctrl+S`)

### 9. Run the App

In terminal:

```bash
python main.py
```

The app should launch with camera access!

## VS Code Extensions (Recommended) 🔌

Install these for better Python development:

1. **Python** (by Microsoft) - Essential
2. **Pylance** - Python language server
3. **Python Indent** - Auto-indentation
4. **autoDocstring** - Generate docstrings

Install: `Ctrl+Shift+X` → Search → Install

## Testing the App 🧪

### Desktop Testing:

1. Run `python main.py`
2. Allow camera access when prompted
3. Click "Start Recognition"
4. Show ASL signs to your webcam
5. Watch it recognize and speak!

### Common Test Signs:

- **Letter A**: Closed fist, thumb on side
- **Letter B**: Flat hand, fingers together, thumb across palm
- **Letter C**: Curved hand forming C shape
- **Hello**: Open hand, salute motion
- **Thank you**: Flat hand on chin, move forward

## Building for Android 📱

### Prerequisites for Android Build:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

**macOS:**
```bash
brew install autoconf automake libtool pkg-config
brew install --cask android-platform-tools
```

### Build APK:

```bash
# First time setup
buildozer init

# Build debug APK
buildozer -v android debug

# APK will be in bin/ folder
```

### Install on Phone:

1. Enable Developer Options on Android
2. Enable USB Debugging
3. Connect phone via USB
4. Run:
   ```bash
   buildozer android debug deploy run
   ```

## Project Structure 📂

```
asl-translator-python/
├── main.py              # Main app code (EDIT THIS)
├── requirements.txt     # Python packages
├── buildozer.spec      # Android build config
├── README.md           # Documentation
├── SETUP_GUIDE.md      # This file
├── .gitignore          # Git ignore rules
├── venv/               # Virtual environment (created)
└── bin/                # Built APKs (after build)
```

## Customization 🎨

### Change Colors:

In `main.py`, find `Window.clearcolor`:

```python
Window.clearcolor = (0.1, 0.1, 0.18, 1)  # Background (R, G, B, A)
```

Change to your preferred color (values 0-1).

### Change Recognition Speed:

Line 127 in `main.py`:

```python
self.recognition_event = Clock.schedule_interval(self.capture_and_recognize, 2)
# Change 2 to 1 for faster (1 second), 3 for slower (3 seconds)
```

### Change Camera:

Line 52 in `main.py`:

```python
index=1  # 1 = front camera, 0 = back camera
```

## Troubleshooting 🔧

### Issue: "No module named 'kivy'"

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Camera not working

**Solution:**
- Check if another app is using camera
- Try changing camera index (0 or 1)
- On Windows: Allow camera access in Settings

### Issue: "API key not valid"

**Solution:**
- Double-check API key in `main.py`
- Ensure no extra spaces
- Get new key from Google AI Studio

### Issue: Import errors on Windows

**Solution:**
```bash
pip install --upgrade setuptools wheel
pip install kivy[base] kivy_examples
```

### Issue: Buildozer fails

**Solution:**
```bash
buildozer android clean
rm -rf .buildozer
buildozer -v android debug
```

## VS Code Tips 💡

### Keyboard Shortcuts:

- `` Ctrl+` `` - Toggle terminal
- `Ctrl+P` - Quick file open
- `Ctrl+Shift+P` - Command palette
- `F5` - Run with debugger
- `Ctrl+/` - Comment/uncomment

### Run with Debugger:

1. Click Run icon (left sidebar)
2. Click "create a launch.json file"
3. Select "Python File"
4. Press `F5` to debug

### Format Code:

1. Install "Black Formatter" extension
2. Right-click in code → "Format Document"
3. Or `Shift+Alt+F`

## Next Steps 🎯

1. ✅ Test on desktop with webcam
2. ✅ Try different ASL signs
3. ✅ Customize colors and timing
4. ✅ Build APK for Android
5. ✅ Test on mobile device
6. ✅ Share with friends!

## Getting Help 💬

- **GitHub Issues**: [Report bugs](https://github.com/aiml34048/asl-translator-python/issues)
- **Email**: aiml34048@gmail.com
- **Kivy Docs**: https://kivy.org/doc/stable/
- **Gemini Docs**: https://ai.google.dev/docs

## Resources 📚

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Gemini API Guide](https://ai.google.dev/tutorials/python_quickstart)
- [ASL Alphabet Reference](https://www.lifeprint.com/asl101/fingerspelling/)

---

**Happy Coding! 🚀**

If you get stuck, check the troubleshooting section or open an issue on GitHub.
