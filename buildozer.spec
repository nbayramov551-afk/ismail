[app]
# (str) Tətbiqin adı
title = Komandir Browser

# (str) Paket adı
package.name = superbrowser

# (str) Paket domeni (istədiyini yaza bilərsən)
package.domain = org.komandir.private

# (str) Sənin əsas kod faylın
source.dir = .

# (list) İstifadə olunacaq fayl uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Tətbiqin versiyası
version = 1.0

# (list) Tətbiqin işləməsi üçün lazım olan modullar
# Bura urllib3 və requests əlavə etdik ki, Telegram-a məlumat göndərə bilsin
requirements = python3,kivy==2.2.1,android,jnius,urllib3,requests

# (str) Ekranın görünüşü (portrait - dik, landscape - yan)
orientation = portrait

# (bool) Tam ekran rejimi
fullscreen = 0

# (list) Android icazələri (Ən vacibi budur!)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Android API səviyyəsi (Android 13 üçün 33 uyğundur)
android.api = 33

# (int) Minimum dəstəklənən Android (Android 5.0+)
android.minapi = 21

# (bool) Google SDK lisenziyalarını avtomatik qəbul et
android.accept_sdk_license = True

# (str) Android log səviyyəsi
log_level = 2

# (str) APK-nın yığılma arxitekturası (Müasir telefonlar üçün arm64-v8a)
android.archs = arm64-v8a

[buildozer]
# (int) Logların ətraflı görünməsi
log_level = 2
