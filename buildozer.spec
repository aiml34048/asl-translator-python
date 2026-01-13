[app]
title = ASL Translator
package.name = asltranslator
package.domain = org.aslapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pillow,google-generativeai,pyttsx3

orientation = portrait
fullscreen = 0

# Android permissions
android.permissions = CAMERA,INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE

# Android API
android.api = 31
android.minapi = 21
android.ndk = 25b

# iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

[buildozer]
log_level = 2
warn_on_root = 1
