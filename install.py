import subprocess
import os
import locale
import ctypes

def get_language():
    """Detects system language, returns 'tr' for Turkish, else 'en'."""
    try:
        # Windows specific: GetUserDefaultUILanguage
        # Primary language ID for Turkish is 0x1f
        windll = ctypes.windll.kernel32
        lang_id = windll.GetUserDefaultUILanguage()
        if (lang_id & 0xFF) == 0x1f: 
            return 'tr'
    except Exception:
        pass
    
    try:
        # Fallback to locale
        lang = locale.getdefaultlocale()[0]
        if lang and lang.lower().startswith('tr'):
            return 'tr'
    except Exception:
        pass
        
    return 'en'

MESSAGES = {
    'en': {
        'error': "Error occurred: {}",
        'unexpected_error': "An unexpected error occurred: {}",
        'press_enter': "Press Enter to continue..."
    },
    'tr': {
        'error': "Hata oluştu: {}",
        'unexpected_error': "Beklenmedik bir hata oluştu: {}",
        'press_enter': "Devam etmek için Enter tuşuna basın..."
    }
}

def t(key, *args):
    lang = get_language()
    msg = MESSAGES.get(lang, MESSAGES['en']).get(key, key)
    return msg.format(*args)

def install():
    try:
        # Run the local run.ps1 script with the -new_theme argument
        script_dir = os.path.dirname(os.path.abspath(__file__))
        run_ps1_path = os.path.join(script_dir, "run.ps1")
        
        # Ensure path is properly escaped for PowerShell if needed
        # We wrap in quotes just in case path has spaces
        ps_command = f"& '{run_ps1_path}' -new_theme"
        
        # Construct the full command to run PowerShell
        # Using -NoProfile and -ExecutionPolicy Bypass to ensure it runs smoothly
        subprocess.run([
            "powershell", 
            "-NoProfile", 
            "-ExecutionPolicy", "Bypass", 
            "-Command", ps_command
        ], check=True)
        
    except subprocess.CalledProcessError as e:
        print(t('error', e))
    except Exception as e:
        print(t('unexpected_error', e))

if __name__ == "__main__":
    install()
    input(t('press_enter'))
