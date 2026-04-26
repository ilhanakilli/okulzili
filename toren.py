import customtkinter as ctk
import os
import glob

class TorenEkrani(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=4, uniform="toren")
        self.grid_columnconfigure(1, weight=6, uniform="toren")
        self.grid_rowconfigure(0, weight=1)
        
        # Marş Listesi
        left = ctk.CTkFrame(self, border_width=2)
        left.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)
        ctk.CTkLabel(left, text="MARŞLAR", font=("Arial", 36, "bold")).pack(pady=20)
        m_sc = ctk.CTkScrollableFrame(left, fg_color="transparent")
        m_sc.pack(fill="both", expand=True, padx=10)
        
        for p in sorted(glob.glob("sesler/marslar/*.*")):
            n = os.path.basename(p)
            ctk.CTkButton(m_sc, text=n[:30], anchor="w", height=60, font=("Arial", 18, "bold"), 
                          command=lambda p=p, n=n: self.controller.load_and_play(p, n)).pack(fill="x", pady=2, padx=5)

        # Medya Kontrol
        right = ctk.CTkFrame(self, border_width=2)
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        ctk.CTkLabel(right, text="MEDYA KONTROL", font=("Arial", 36, "bold")).pack(pady=10)
        
        self.lbl_playing = ctk.CTkLabel(right, text="Çalan: -", font=("Arial", 22, "italic"), wraplength=500)
        self.lbl_playing.pack(pady=10)
        
        self.music_slider = ctk.CTkSlider(right, from_=0, to=100, command=self.controller.slide_music, height=35)
        self.music_slider.set(0)
        self.music_slider.pack(fill="x", padx=40, pady=20)
        
        self.lbl_time = ctk.CTkLabel(right, text="00:00 / 00:00", font=("Arial", 40, "bold"), text_color="#e67e22")
        self.lbl_time.pack()

        btn_f = ctk.CTkFrame(right, fg_color="transparent")
        btn_f.pack(pady=20)
        ctk.CTkButton(btn_f, text="⏸ DURAKLAT", fg_color="#f1c40f", text_color="black", width=160, height=80, 
                      font=("Arial", 18, "bold"), command=self.controller.scheduler.player.pause).pack(side="left", padx=10)
        ctk.CTkButton(btn_f, text="▶ OYNAT", fg_color="#2ecc71", width=160, height=80, 
                      font=("Arial", 18, "bold"), command=self.controller.scheduler.player.play).pack(side="left", padx=10)
        ctk.CTkButton(btn_f, text="⏹ DURDUR", fg_color="#e74c3c", width=160, height=80, 
                      font=("Arial", 18, "bold"), command=self.controller.stop_and_reset).pack(side="left", padx=10)

        # USB Listesi
        self.usb_scroll = ctk.CTkScrollableFrame(right, label_text="USB İÇERİĞİ", label_font=("Arial", 22, "bold"))
        self.usb_scroll.pack(fill="both", expand=True, padx=20, pady=10)
        
        f_btn = ctk.CTkFrame(right, fg_color="transparent")
        f_btn.pack(fill="x", pady=10)
        # USB Tarat butonu controller üzerindeki refresh_usb_list'i çağırır
        ctk.CTkButton(f_btn, text="USB TARAT", height=60, font=("Arial", 18, "bold"), command=self.controller.refresh_usb_list).pack(side="left", expand=True, padx=5)
        ctk.CTkButton(f_btn, text="ANA EKRANA DÖN", height=60, font=("Arial", 18, "bold"), fg_color="#7f8c8d", command=self.controller.show_dashboard).pack(side="left", expand=True, padx=5)
