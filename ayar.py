import customtkinter as ctk
import os, glob

class AyarEkrani(ctk.CTkFrame):
    def __init__(self, parent, controller, conf):
        super().__init__(parent)
        self.controller, self.conf = controller, conf
        self.color_palette = [
            "#000000", "#ffffff", "#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#1abc9c", "#3498db", "#9b59b6", "#34495e",
            "#c0392b", "#d35400", "#f39c12", "#27ae60", "#16a085", "#2980b9", "#8e44ad", "#2c3e50", "#95a5a6", "#7f8c8d",
            "#ff7675", "#fab1a0", "#ffeaa7", "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#b2bec3", "#636e72"
        ]
        self.visual_settings, self.hour_entries, self.sound_widgets = {}, [], {}
        self.setup_ui()

    def setup_ui(self):
        t_f = self.controller.text_fume
        top = ctk.CTkFrame(self); top.pack(fill="x", padx=10, pady=10)
        ctk.CTkButton(top, text=" < GERİ", fg_color="#95a5a6", width=150, height=50, font=("Arial", 18, "bold"), command=self.controller.show_dashboard).pack(side="left", padx=15)
        ctk.CTkLabel(top, text="SİSTEM AYARLARI", font=("Arial", 32, "bold"), text_color=t_f).pack(side="left", padx=20)
        
        # SİSTEMİ KAPAT BUTONU (ORTALANMIŞ)
        ctk.CTkButton(top, text="SİSTEMİ KAPAT", fg_color="#e74c3c", width=200, height=50, font=("Arial", 18, "bold"), command=self.controller.exit_application).pack(side="left", expand=True)
        
        ctk.CTkButton(top, text="KAYDET", fg_color="#2ecc71", width=150, height=50, font=("Arial", 18, "bold"), command=self.controller.save_all_settings).pack(side="right", padx=15)
        
        self.tabs = ctk.CTkTabview(self)
        self.tabs._segmented_button.configure(font=("Arial", 18, "bold"))
        self.tabs.pack(fill="both", expand=True, padx=10, pady=5)
        
        t_hours = self.tabs.add("Ders Saatleri")
        t_sounds = self.tabs.add("Zil Sesleri")
        t_visual = self.tabs.add("Görünüm")
        t_slide = self.tabs.add("Slayt Ayarları")
        
        # --- DERS SAATLERİ ---
        sc = ctk.CTkScrollableFrame(t_hours); sc.pack(fill="both", expand=True)
        h_f = ("Arial", 16, "bold")
        ctk.CTkLabel(sc, text="Ders", width=100, font=h_f, text_color=t_f).grid(row=0, column=0)
        ctk.CTkLabel(sc, text="Öğrenci Giriş", width=120, font=h_f, text_color=t_f).grid(row=0, column=1)
        ctk.CTkLabel(sc, text="Öğretmen Giriş", width=120, font=h_f, text_color=t_f).grid(row=0, column=2)
        ctk.CTkLabel(sc, text="Çıkış (Zil)", width=120, font=h_f, text_color=t_f).grid(row=0, column=3)
        for idx in range(15):
            row = idx + 1
            ctk.CTkLabel(sc, text=f"{idx+1}. Ders", width=100, font=("Arial", 15, "bold"), text_color=t_f).grid(row=row, column=0, padx=10, pady=8)
            e_s, e_t, e_e = ctk.CTkEntry(sc, width=120, height=40, font=("Arial", 16), justify="center"), ctk.CTkEntry(sc, width=120, height=40, font=("Arial", 16), justify="center"), ctk.CTkEntry(sc, width=120, height=40, font=("Arial", 16), justify="center")
            e_s.grid(row=row, column=1, padx=8); e_t.grid(row=row, column=2, padx=8); e_e.grid(row=row, column=3, padx=8)
            self.hour_entries.append({"name": f"{idx+1}. Ders", "s": e_s, "t": e_t, "e": e_e})
        
        self.opt_apply = ctk.CTkOptionMenu(t_hours, width=250, height=45, font=("Arial", 16, "bold"), values=["SEÇİNİZ", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar", "Hafta İçi", "Tüm Günler"], command=self.controller.load_selected_day_hours)
        self.opt_apply.pack(pady=(15, 5))
        ctk.CTkLabel(t_hours, text="ÖĞLE ARASI TENEFFÜSÜ", font=("Arial", 18, "bold"), text_color=t_f).pack(pady=(10, 0))
        self.opt_lunch_break = ctk.CTkOptionMenu(t_hours, width=250, height=45, font=("Arial", 16, "bold"), values=["SEÇİNİZ"] + [f"{i}. TENEFFÜS" for i in range(1, 15)])
        self.opt_lunch_break.set("SEÇİNİZ")
        self.opt_lunch_break.pack(pady=(5, 15))
        ctk.CTkButton(t_hours, text="TABLOYU TEMİZLE", fg_color="#e74c3c", width=200, height=40, font=("Arial", 14, "bold"), command=self.clear_schedule_table).pack(pady=5)
        
        # --- ZİL SESLERİ ---
        s_sc = ctk.CTkScrollableFrame(t_sounds); s_sc.pack(fill="both", expand=True)
        melodiler = [os.path.basename(x) for x in glob.glob("sesler/zilmelodileri/*.*")]
        for k, l in [("student", "Öğrenci"), ("teacher", "Öğretmen"), ("exit", "Çıkış")]:
            r = ctk.CTkFrame(s_sc); r.pack(fill="x", pady=12, padx=15)
            ctk.CTkLabel(r, text=f"{l} Zili:", width=150, font=("Arial", 18, "bold"), anchor="w", text_color=t_f).pack(side="left", padx=10)
            o = ctk.CTkOptionMenu(r, values=melodiler, width=300, height=45, font=("Arial", 16)); o.set(self.conf["current_sounds"].get(k, "")); o.pack(side="left", padx=10)
            ctk.CTkButton(r, text="▶", width=60, height=45, font=("Arial", 20), fg_color="#3498db", command=lambda p=o: self.controller.load_and_play(f"sesler/zilmelodileri/{p.get()}", p.get())).pack(side="left", padx=5)
            ctk.CTkButton(r, text="■", width=60, height=45, font=("Arial", 20), fg_color="#e67e22", command=self.controller.scheduler.player.stop).pack(side="left", padx=5)
            s = ctk.CTkSlider(r, from_=0, to=1, width=200); s.set(self.conf["volumes"].get(k, 0.8)); s.pack(side="right", padx=20); self.sound_widgets[k] = (o, s)
        
        m_fr = ctk.CTkFrame(s_sc, fg_color="#f39c12"); m_fr.pack(fill="x", pady=20, padx=15)
        ctk.CTkLabel(m_fr, text="MÜZİK YAYINI SES SEVİYESİ", font=("Arial", 18, "bold"), text_color="white").pack(pady=5)
        self.music_vol_slider = ctk.CTkSlider(m_fr, from_=0, to=100, width=500); self.music_vol_slider.set(self.conf.get("music_volume", 50)); self.music_vol_slider.pack(pady=10)

        # --- GÖRÜNÜM ---
        gv_sc = ctk.CTkScrollableFrame(t_visual); gv_sc.pack(fill="both", expand=True)
        ctk.CTkLabel(gv_sc, text="TEMA SEÇİMİ", font=("Arial", 16, "bold"), text_color=t_f).pack(pady=(15, 0))
        self.opt_theme = ctk.CTkOptionMenu(gv_sc, width=200, height=40, font=("Arial", 16), values=["beyaz", "koyu"]); self.opt_theme.set(self.conf.get("theme", "beyaz")); self.opt_theme.pack(pady=(5, 15))
        ctk.CTkLabel(gv_sc, text="OKUL ADI", font=("Arial", 16, "bold"), text_color=t_f).pack(pady=(5, 0))
        self.ent_school = ctk.CTkEntry(gv_sc, width=500, height=45, font=("Arial", 18)); self.ent_school.insert(0, self.conf.get("school_name", "")); self.ent_school.pack(pady=(5, 15))
        ctk.CTkLabel(gv_sc, text="KAYAN DUYURU METNİ", font=("Arial", 16, "bold"), text_color=t_f).pack(pady=(5, 0))
        self.ent_ann = ctk.CTkEntry(gv_sc, width=500, height=45, font=("Arial", 18)); self.ent_ann.insert(0, self.conf.get("announcement", "")); self.ent_ann.pack(pady=(5, 15))
        self.create_color_pickers(gv_sc, {"clock": "Saat", "timer": "Sayaç", "lesson": "Ders Bilgisi", "date": "Tarih", "announcement": "Duyuru"}, t_f)

        # --- SLAYT AYARLARI ---
        sl_sc = ctk.CTkScrollableFrame(t_slide); sl_sc.pack(fill="both", expand=True)
        f_int = ctk.CTkFrame(sl_sc); f_int.pack(fill="x", pady=15, padx=15)
        ctk.CTkLabel(f_int, text="Slayt Geçiş Süresi (Saniye):", font=("Arial", 18, "bold"), text_color=t_f).pack(side="left", padx=10)
        self.slide_interval_slider = ctk.CTkSlider(f_int, from_=3, to=60, number_of_steps=57, width=300); self.slide_interval_slider.set(self.conf.get("slide_interval", 10)); self.slide_interval_slider.pack(side="left", padx=20)
        self.lbl_interval_val = ctk.CTkLabel(f_int, text=f"{int(self.slide_interval_slider.get())} sn", font=("Arial", 18, "bold"), text_color=t_f); self.lbl_interval_val.pack(side="left")
        self.slide_interval_slider.configure(command=lambda v: self.lbl_interval_val.configure(text=f"{int(v)} sn"))
        self.create_color_pickers(sl_sc, {"slide_info": "Slayt Yazı Rengi", "slide_bg": "Yazı Arka Planı"}, t_f)

        # ÇİZİMİ ZORLA (Render sorununu çözer)
        self.update()

    def create_color_pickers(self, parent_frame, labels_dict, text_col):
        for k, l_t in labels_dict.items():
            fr = ctk.CTkFrame(parent_frame); fr.pack(fill="x", pady=10, padx=15)
            ctk.CTkLabel(fr, text=l_t, width=150, font=("Arial", 16, "bold"), anchor="w", text_color=text_col).pack(side="left")
            sz = ctk.CTkEntry(fr, width=70, height=40, font=("Arial", 16), justify="center"); sz.insert(0, str(self.conf["font_sizes"].get(k, 100))); sz.pack(side="left", padx=10)
            pal_scroll = ctk.CTkScrollableFrame(fr, orientation="horizontal", height=50, fg_color="transparent")
            pal_scroll.pack(side="left", fill="x", expand=True, padx=5)
            c_c = self.conf["custom_colors"].get(k, "#ffffff")
            self.visual_settings[k] = {"size": sz, "pal_fr": pal_scroll, "current_color": c_c}
            for c_h in self.color_palette:
                btn = ctk.CTkButton(pal_scroll, text="", fg_color=c_h, width=35, height=35, corner_radius=5, border_width=3 if c_h == c_c else 0, border_color="white", command=lambda key=k, h_v=c_h: self.select_color(key, h_v))
                btn.pack(side="left", padx=3)

    def select_color(self, category, hex_val):
        for btn in self.visual_settings[category]["pal_fr"].winfo_children():
            btn.configure(border_width=0)
            if btn.cget("fg_color") == hex_val: btn.configure(border_width=3, border_color="white")
        self.visual_settings[category]["current_color"] = hex_val

    def clear_schedule_table(self):
        for e in self.hour_entries: e["s"].delete(0, "end"); e["t"].delete(0, "end"); e["e"].delete(0, "end")
