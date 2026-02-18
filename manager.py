import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import sys
import ctypes
import locale
import install
import uninstall

class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl
        
    def write(self, string):
        self.output.insert(tk.END, string)
        self.output.see(tk.END)
        
    def flush(self):
        pass

class SpotifyManagerApp:
    def __init__(self, root):
        self.root = root
        self.lang = self.get_language()
        self.setup_ui()
        
    def get_language(self):
        """Detects system language, returns 'tr' for Turkish, else 'en'."""
        try:
            windll = ctypes.windll.kernel32
            lang_id = windll.GetUserDefaultUILanguage()
            if (lang_id & 0xFF) == 0x1f:
                return 'tr'
        except Exception:
            pass
        
        try:
            lang = locale.getdefaultlocale()[0]
            if lang and lang.lower().startswith('tr'):
                return 'tr'
        except Exception:
            pass
            
        return 'en'

    def get_text(self, key):
        texts = {
            'en': {
                'title': "Spotify Manager",
                'install_btn': "Install / Patch",
                'uninstall_btn': "Uninstall / Remove",
                'status_ready': "Ready",
                'status_running': "Running...",
                'status_done': "Done",
                'log_label': "Logs:"
            },
            'tr': {
                'title': "Spotify Yöneticisi",
                'install_btn': "Yükle / Yama Yap",
                'uninstall_btn': "Kaldır / Temizle",
                'status_ready': "Hazır",
                'status_running': "İşlem yapılıyor...",
                'status_done': "Tamamlandı",
                'log_label': "Kayıtlar:"
            }
        }
        return texts.get(self.lang, texts['en']).get(key, key)

    def setup_ui(self):
        self.root.title(self.get_text('title'))
        self.root.geometry("500x400")
        
        # Style
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Buttons Frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.install_btn = ttk.Button(btn_frame, text=self.get_text('install_btn'), command=self.run_install)
        self.install_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.uninstall_btn = ttk.Button(btn_frame, text=self.get_text('uninstall_btn'), command=self.run_uninstall)
        self.uninstall_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Log Area
        log_label = ttk.Label(main_frame, text=self.get_text('log_label'))
        log_label.pack(anchor=tk.W)
        
        self.log_area = scrolledtext.ScrolledText(main_frame, height=15)
        self.log_area.pack(fill=tk.BOTH, expand=True)
        
        # Redirect stdout
        sys.stdout = RedirectText(self.log_area)
        sys.stderr = RedirectText(self.log_area)

    def run_in_thread(self, target_func):
        self.install_btn.config(state=tk.DISABLED)
        self.uninstall_btn.config(state=tk.DISABLED)
        self.log_area.insert(tk.END, f"\n--- {self.get_text('status_running')} ---\n")
        
        def wrapper():
            try:
                target_func()
            except Exception as e:
                print(f"GUI Error: {e}")
            finally:
                self.root.after(0, self.on_task_done)
                
        thread = threading.Thread(target=wrapper)
        thread.daemon = True
        thread.start()

    def on_task_done(self):
        self.install_btn.config(state=tk.NORMAL)
        self.uninstall_btn.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, f"\n--- {self.get_text('status_done')} ---\n")
        self.log_area.see(tk.END)

    def run_install(self):
        self.run_in_thread(install.install)

    def run_uninstall(self):
        self.run_in_thread(uninstall.uninstall)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpotifyManagerApp(root)
    root.mainloop()
