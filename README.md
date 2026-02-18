This is not the original repository. This is only the Python version of the real repository, and everything fully belongs to the original repository owner.
https://github.com/r3mz0/Spotify-win

icinde ad-block bunulur 
t includes a built-in ad blocker.

# Python Scripts for Spotify-win / Spotify-win için Python Scriptleri

[English](#english) | [Türkçe](#türkçe)

---

## English

This folder contains Python scripts to manage Spotify installation and uninstallation, mirroring the functionality of the original batch files but with added features like localization and a GUI manager.

### Files

- **`install.py`**: 
  - Downloads and installs Spotify/Spicetify/SpotX themes.
  - Automatically detects system language (TR/EN) for output messages.
  - Uses the local `run.ps1` script for execution.

- **`uninstall.py`**: 
  - Removes Spotify, Spicetify, SpotX, and related data from `%AppData%` and `%Temp%`.
  - Automatically detects system language (TR/EN).

- **`manager.py`**: 
  - A simple Graphical User Interface (GUI) to run `install.py` and `uninstall.py`.
  - Displays logs in the window.

### Usage

#### Prerequisites
- Python 3.x installed.
- Windows OS (PowerShell required for installation).

#### Running via GUI
Double-click `manager.py` or run:
```bash
python manager.py
```

#### Running Scripts Manually
To install:
```bash
python install.py
```

To uninstall:
```bash
python uninstall.py
```

### Localization
The scripts automatically detect if your system language is Turkish. If so, they will display messages in Turkish. Otherwise, they default to English.

### Requirements
No external Python libraries are required. The scripts use standard libraries included with Python.

---

## Türkçe

Bu klasör, Spotify kurulumu ve kaldırılmasını yönetmek için Python scriptlerini içerir. Orijinal batch dosyalarının işlevselliğini yansıtır ancak yerelleştirme ve GUI yöneticisi gibi ek özellikler sunar.

### Dosyalar

- **`install.py`**: 
  - Spotify/Spicetify/SpotX temalarını indirir ve yükler.
  - Çıktı mesajları için sistem dilini (TR/EN) otomatik olarak algılar.
  - Çalıştırma için yerel `run.ps1` scriptini kullanır.

- **`uninstall.py`**: 
  - Spotify, Spicetify, SpotX ve ilgili verileri `%AppData%` ve `%Temp%` klasörlerinden kaldırır.
  - Sistem dilini (TR/EN) otomatik olarak algılar.

- **`manager.py`**: 
  - `install.py` ve `uninstall.py` dosyalarını çalıştırmak için basit bir Grafiksel Kullanıcı Arayüzü (GUI).
  - Logları pencere içinde gösterir.

### Kullanım

#### Gereksinimler
- Python 3.x kurulu olmalıdır.
- Windows İşletim Sistemi (Kurulum için PowerShell gereklidir).

#### GUI ile Çalıştırma
`manager.py` dosyasına çift tıklayın veya şunu çalıştırın:
```bash
python manager.py
```

#### Scriptleri Manuel Çalıştırma
Yüklemek için:
```bash
python install.py
```

Kaldırmak için:
```bash
python uninstall.py
```

### Yerelleştirme
Scriptler, sistem dilinizin Türkçe olup olmadığını otomatik olarak algılar. Eğer öyleyse, mesajları Türkçe olarak görüntüler. Aksi takdirde varsayılan olarak İngilizce kullanır.

### Gereksinimler
Harici bir Python kütüphanesi gerekmez. Scriptler Python ile birlikte gelen standart kütüphaneleri kullanır.
