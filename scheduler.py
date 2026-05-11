import vlc
import datetime
import os
from config_manager import load_config

# Zamanlama ve zil çalma mantığını yöneten sınıf.
class BellScheduler:
    def __init__(self):
        self.instance = vlc.Instance('--no-video', '--quiet')
        self.player = self.instance.media_player_new()
        self.music_player = self.instance.media_player_new()

    def get_status(self):
        conf = load_config()
        now = datetime.datetime.now()
        days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day_key = days_list[now.weekday()] 
        schedule = conf["schedule"].get(day_key, [])

        if not schedule or not any(l.get("student") for l in schedule):
            return "PROGRAM GİRİLMEMİŞ", "00:00", "idle"

        active_schedule = [l for l in schedule if l.get("student") and l.get("exit")]
        
        if active_schedule:
            try:
                first_start = min(
                    datetime.datetime.strptime(l["student"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)
                    for l in active_schedule
                )
                if now < first_start:
                    diff = first_start - now
                    return "GÜNAYDIN", f"{diff.seconds//60:02d}:{diff.seconds%60:02d}", "greeting"
            except Exception:
                pass

        for i, lesson in enumerate(active_schedule):
            try:
                s_time = datetime.datetime.strptime(lesson["student"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)
                t_val = lesson.get("teacher") if lesson.get("teacher") else lesson["student"]
                t_time = datetime.datetime.strptime(t_val, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
                e_time = datetime.datetime.strptime(lesson["exit"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)

                # Yeni Kısa Şablon: "X. DERS BAŞLIYOR :)"
                if s_time <= now < t_time:
                    diff = t_time - now
                    lesson_num = lesson['name'].split('.')[0]
                    return f"{lesson_num}. DERS BAŞLIYOR :)", f"{diff.seconds//60:02d}:{diff.seconds%60:02d}", "preparing"

                if t_time <= now <= e_time:
                    diff = e_time - now
                    lesson_num = lesson['name'].split('.')[0]
                    return f"{lesson_num}. DERS (DERSTEYİZ)", f"{diff.seconds//60:02d}:{diff.seconds%60:02d}", "lesson"

                if i < len(active_schedule) - 1:
                    next_s = datetime.datetime.strptime(active_schedule[i+1]["student"], "%H:%M").replace(year=now.year, month=now.month, day=now.day)
                    if e_time < now < next_s:
                        diff = next_s - now
                        lunch_breaks = conf.get("lunch_breaks", {})
                        lunch_break = lunch_breaks.get(day_key, 4)
                        break_index = i + 1
                        if break_index == lunch_break:
                            teneffus_adi = "ÖĞLE ARASI"
                        else:
                            teneffus_adi = f"{break_index}. TENEFFÜS"
                        return teneffus_adi, f"{diff.seconds//60:02d}:{diff.seconds%60:02d}", "intermission"
            except: continue
        return "EĞİTİM SONA ERDİ", "00:00", "idle"

    def check_and_ring(self):
        conf = load_config()
        if not conf.get("system_enabled", True): return False
        now_hm = datetime.datetime.now().strftime("%H:%M")
        days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day_key = days_list[datetime.datetime.now().weekday()]
        
        for l in conf["schedule"].get(day_key, []):
            if l.get("student") == now_hm: return self.play_bell("student")
            if l.get("teacher") == now_hm: return self.play_bell("teacher")
            if l.get("exit") == now_hm: return self.play_bell("exit")
        return False

    def play_bell(self, bell_type):
        try:
            if self.music_player.is_playing(): self.music_player.stop()
            conf = load_config()
            sound_name = conf["current_sounds"].get(bell_type)
            volume = conf["volumes"].get(bell_type, 0.8)
            path = os.path.join(os.path.dirname(__file__), "sesler", "zilmelodileri", sound_name)
            if os.path.exists(path):
                media = self.instance.media_new(path)
                self.player.set_media(media)
                self.player.audio_set_volume(int(volume * 100))
                self.player.play()
                return True
            return False
        except: return False
