import json
import shutil
import os

CONFIG_FILE = "config.json"
BACKUP_DIR = "backups"

# Konfigürasyon dosyasını oku/yaz ve basit yedekleme işlemleri yap.

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {
            "system_enabled": True, "music_active": True, "slide_active": False,
            "theme": "koyu", "school_name": "KONURALP ORTAOKULU", "announcement": "DUYURU METNİ",
            "slide_interval": 10, "music_volume": 68, "master_volume": 100,
            "font_sizes": {"clock": 140, "timer": 280, "date": 60, "announcement": 45, "lesson": 80, "slide_info": 40},
            "custom_colors": {"clock": "#2E4053", "announcement": "#0E6251", "date": "#2C3E50", "timer": "#922B21", "lesson": "#2C3E50", "slide_info": "#ffffff"},
            "current_sounds": {"student": "", "teacher": "", "exit": ""},
            "volumes": {"student": 1, "teacher": 1, "exit": 1},
            "lunch_breaks": {d: 4 for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]},
            "schedule": {d: [] for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]}
        }
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    shutil.copy(CONFIG_FILE, os.path.join(BACKUP_DIR, "config_backup.json"))

def export_backup(target_path):
    shutil.copy(CONFIG_FILE, target_path)

def import_backup(source_path):
    shutil.copy(source_path, CONFIG_FILE)
    return load_config()
