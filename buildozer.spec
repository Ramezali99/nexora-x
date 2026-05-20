[app]

title = Nexora X

package.name = nexora

package.domain = org.nexora

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

# Android API
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b

# Accept SDK licenses automatically
android.accept_sdk_license = True

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Enable AndroidX
android.enable_androidx = True


[buildozer]

log_level = 2

warn_on_root = 0
