from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread
from android.permissions import request_permissions, Permission

# Android hissələri
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
KeyEvent = autoclass('android.view.KeyEvent')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class BrowserClient(WebViewClient):
    # Linklərə klikləyəndə brauzerin içində açılması üçün
    def shouldOverrideUrlLoading(self, view, url):
        return False

class SuperBrowser(App):
    def build(self):
        self.webview = None
        request_permissions([Permission.INTERNET]) # İcazə istəyirik
        self.create_webview()
        # Geri düyməsini tutmaq üçün
        Activity.bind(onKeyDown=self.on_key_down)
        return Widget() # Boş widget, çünki WebView üstə gələcək

    @run_on_ui_thread
    def create_webview(self):
        self.webview = WebView(Activity)
        settings = self.webview.getSettings()
        settings.setJavaScriptEnabled(True) # Bütün saytları açmaq üçün
        settings.setDomStorageEnabled(True) # Yaddaş dəstəyi
        
        # Reklam qarşısını almaq və ya özəlləşdirmək istəsən bura baxarıq
        self.webview.setWebViewClient(BrowserClient())
        
        # BAŞLANĞIC SAYTI (Buranı istədiyin kimi dəyiş)
        self.webview.loadUrl('https://www.google.com') 
        
        Activity.setContentView(self.webview)

    def on_key_down(self, window, keycode, scancode):
        # Əgər geri düyməsi basılıbsa və tarixçə varsa, geri qayıt
        if keycode == 4 and self.webview and self.webview.canGoBack():
            self.webview.goBack()
            return True
        return False

    def on_stop(self):
        Activity.unbind(onKeyDown=self.on_key_down)

if __name__ == '__main__':
    SuperBrowser().run()
  
