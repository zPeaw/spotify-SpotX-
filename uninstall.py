import os
import shutil
import glob
import locale
import ctypes

def get_language():
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

MESSAGES = {
    'en': {
        'appdata_error': "Error: APPDATA environment variable not found.",
        'success': "Successfully removed.",
        'press_enter': "Press Enter to continue..."
    },
    'tr': {
        'appdata_error': "Hata: APPDATA ortam değişkeni bulunamadı.",
        'success': "Başarıyla kaldırıldı.",
        'press_enter': "Devam etmek için Enter tuşuna basın..."
    }
}

def t(key):
    lang = get_language()
    return MESSAGES.get(lang, MESSAGES['en']).get(key, key)

def force_remove(path):
    """
    Attempts to remove a file or directory. 
    Equivalent to del /s /q or rd /s /q
    """
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except Exception as e:
        pass

def uninstall():
    appdata = os.environ.get('APPDATA')
    temp = os.environ.get('TEMP')
    
    if not appdata:
        print(t('appdata_error'))
        return

    spotify_dir = os.path.join(appdata, 'Spotify')
    
    # 1. dpapi.dll
    dpapi_path = os.path.join(spotify_dir, 'dpapi.dll')
    if os.path.exists(dpapi_path):
        force_remove(dpapi_path)

    # 2. Spotify.bak -> Spotify.exe
    spotify_bak = os.path.join(spotify_dir, 'Spotify.bak')
    spotify_exe = os.path.join(spotify_dir, 'Spotify.exe')
    
    if os.path.exists(spotify_bak):
        if os.path.exists(spotify_exe):
            force_remove(spotify_exe)
        try:
            shutil.move(spotify_bak, spotify_exe)
        except Exception:
            pass

    # 3. config.ini
    config_ini = os.path.join(spotify_dir, 'config.ini')
    if os.path.exists(config_ini):
        force_remove(config_ini)

    # 4. xpui.bak -> xpui.spa
    apps_dir = os.path.join(spotify_dir, 'Apps')
    xpui_bak = os.path.join(apps_dir, 'xpui.bak')
    xpui_spa = os.path.join(apps_dir, 'xpui.spa')
    
    if os.path.exists(xpui_bak):
        if os.path.exists(xpui_spa):
            force_remove(xpui_spa)
        try:
            shutil.move(xpui_bak, xpui_spa)
        except Exception:
            pass

    # 5. blockthespot_log.txt
    log_file = os.path.join(spotify_dir, 'blockthespot_log.txt')
    if os.path.exists(log_file):
        force_remove(log_file)

    # 6. SpotX_Temp* in TEMP
    if temp:
        # Values like %temp%\SpotX_Temp*
        pattern = os.path.join(temp, "SpotX_Temp*")
        for folder in glob.glob(pattern):
            force_remove(folder)

    print(t('success'))

if __name__ == "__main__":
    uninstall()
    input(t('press_enter'))
