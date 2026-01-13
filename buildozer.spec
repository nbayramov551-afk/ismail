[app]
title = Komandir Browser
package.name = superbrowser
package.domain = org.komandir.private
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Telegram və Brauzer modulları
requirements = python3,kivy==2.2.1,android,jnius,urllib3,requests

orientation = portrait
fullscreen = 0

# Android İcazələri
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Stabil API Ayarları
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

log_level = 2

[buildozer]
log_level = 2
