[app]
# Tətbiqin adı (Dostların telefonunda belə görünəcək)
title = Komandir Browser

# Paket adı (Bu sənin gizli imzan olacaq)
package.name = superbrowser
package.domain = org.komandir_private

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,android,pyjnius

# Tam ekran rejimi
orientation = portrait
fullscreen = 1

# Android icazələri (Hər şeyi aça bilməsi üçün)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Versiya ayarları
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
p4a.branch = master
o
