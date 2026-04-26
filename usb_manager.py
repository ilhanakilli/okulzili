import os
import glob

class USBManager:
    @staticmethod
    def get_usb_base_path():
        try:
            user = os.getlogin()
        except:
            user = "konuralp"
        
        usb_base = f"/media/{user}/"
        if os.path.exists(usb_base):
            mounts = glob.glob(os.path.join(usb_base, "*"))
            if mounts:
                return mounts[0]
        return None

    @staticmethod
    def get_intermission_music():
        usb_path = USBManager.get_usb_base_path()
        if not usb_path:
            return []
        
        music_dir = os.path.join(usb_path, "muzikyayini")
        if os.path.exists(music_dir):
            files = glob.glob(os.path.join(music_dir, "*.mp3")) + glob.glob(os.path.join(music_dir, "*.wav"))
            return files
        return []

    @staticmethod
    def get_slide_images():
        usb_path = USBManager.get_usb_base_path()
        if not usb_path:
            return []
        
        slide_dir = os.path.join(usb_path, "slayt")
        if os.path.exists(slide_dir):
            extensions = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG')
            files = []
            for ext in extensions:
                files.extend(glob.glob(os.path.join(slide_dir, ext)))
            return sorted(files)
        return []
