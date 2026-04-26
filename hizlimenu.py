import customtkinter as ctk

class HizliMenu(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.btn_font = ("Arial", 20, "bold")
        self.std_height = 65 
        self.large_height = 75
        self.setup_ui()

    def setup_ui(self):
        # USB GÜVENLE ÇIKAR BUTONU
        ctk.CTkButton(self, text="USB GÜVENLE ÇIKAR", height=self.std_height, font=self.btn_font, 
                      fg_color="#e74c3c", hover_color="#c0392b", text_color="white", 
                      command=self.controller.eject_usb).pack(fill="x", padx=5, pady=(10, 5))

        ctk.CTkButton(self, text="TÖREN MODU", height=self.std_height, font=self.btn_font, 
                      fg_color="#e67e22", text_color=self.controller.text_fume, 
                      command=self.controller.show_ceremony).pack(fill="x", padx=5, pady=5)
        
        self.btn_settings = ctk.CTkButton(self, text="AYARLAR", height=self.std_height, font=self.btn_font, 
                                          text_color="white", command=self.controller.show_settings)
        self.btn_settings.pack(fill="x", padx=5, pady=5)
        
        self.btn_slide = ctk.CTkButton(self, text="SLAYT MODU", height=self.std_height, font=self.btn_font, 
                                       fg_color="#95a5a6", text_color=self.controller.text_fume, 
                                       command=self.controller.toggle_slide)
        self.btn_slide.pack(fill="x", padx=5, pady=5)

        self.btn_music = ctk.CTkButton(self, text="MÜZİK YAYINI", height=self.std_height, font=self.btn_font, 
                                       fg_color="#95a5a6", text_color=self.controller.text_fume, 
                                       command=self.controller.toggle_music)
        self.btn_music.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(self, text="MANUEL ZİLLER", font=("Arial", 18, "bold"), 
                     text_color=self.controller.text_fume).pack(pady=10)
        
        for l, s, c in [("ÖĞRENCİ", "student", "#3498db"), ("ÖĞRETMEN", "teacher", "#2ecc71"), ("ÇIKIŞ", "exit", "#f39c12")]:
            r = ctk.CTkFrame(self, fg_color="transparent")
            r.pack(fill="x", pady=3)
            ctk.CTkButton(r, text=l, fg_color=c, height=60, font=self.btn_font, 
                          text_color=self.controller.text_fume, 
                          command=lambda s=s: self.controller.scheduler.play_bell(s)).pack(side="left", expand=True, fill="x", padx=(0,2))
            ctk.CTkButton(r, text="⏹", fg_color="#e74c3c", width=60, height=60, font=("Arial", 22, "bold"), 
                          text_color=self.controller.text_fume, 
                          command=self.controller.scheduler.player.stop).pack(side="left")

        ctk.CTkLabel(self, text="ACİL DURUM", font=("Arial", 18, "bold"), text_color="#e74c3c").pack(pady=(15, 5))
        siren_row = ctk.CTkFrame(self, fg_color="transparent")
        siren_row.pack(fill="x", pady=3)
        self.btn_siren = ctk.CTkButton(siren_row, text="🚨 SİREN ÇAL", fg_color="#000000", height=self.large_height, 
                                       font=self.btn_font, text_color="white", command=self.controller.play_siren)
        self.btn_siren.pack(side="left", expand=True, fill="x", padx=(0,2))
        ctk.CTkButton(siren_row, text="⏹", fg_color="#e74c3c", width=70, height=self.large_height, font=("Arial", 26, "bold"), 
                      text_color=self.controller.text_fume, command=self.controller.scheduler.player.stop).pack(side="left")

        self.btn_sys_toggle = ctk.CTkButton(self, text="", height=self.large_height, font=self.btn_font, 
                                            text_color=self.controller.text_fume, command=self.controller.toggle_system)
        self.btn_sys_toggle.pack(fill="x", padx=5, pady=20)

        ctk.CTkLabel(self, text="SİSTEM SES SEVİYESİ", font=("Arial", 14, "bold"), 
                     text_color=self.controller.text_fume).pack(pady=(10, 0))
        self.slider_sys_vol = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100, height=20, 
                                            command=self.controller.set_system_volume)
        self.slider_sys_vol.set(self.controller.get_system_volume())
        self.slider_sys_vol.pack(fill="x", padx=10, pady=(5, 20))

        self.side_info_frame = ctk.CTkFrame(self, fg_color="transparent", height=120)
        self.side_info_frame.pack_propagate(False)
        self.side_info_frame.pack(fill="x", pady=10)
        self.lbl_side_day = ctk.CTkLabel(self.side_info_frame, text="", font=("Arial", 20, "bold"), 
                                         text_color=self.controller.text_fume)
        self.lbl_side_day.pack(pady=(10, 0))
        # SAAT YAZI BOYUTU 46
        self.lbl_side_clock = ctk.CTkLabel(self.side_info_frame, text="", font=("Arial", 46, "bold"), 
                                           text_color=self.controller.text_fume)
        self.lbl_side_clock.pack(pady=(0, 10))
