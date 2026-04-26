import customtkinter as ctk
import time
from PIL import Image, ImageOps
from usb_manager import USBManager

class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, conf):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.conf = conf
        self.slide_images = []
        self.current_slide_idx = 0
        self.last_slide_time = 0
        self.setup_ui()

    def setup_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.standard_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.standard_frame.grid(row=0, column=0, sticky="nsew")
        
        f = self.conf.get("font_sizes", {})
        c = self.conf.get("custom_colors", {})

        self.lbl_day = ctk.CTkLabel(self.standard_frame, text="", font=("Arial", int(f.get("date", 70)), "bold"), text_color=c.get("date"))
        self.lbl_day.pack(pady=(10, 0))
        self.lbl_lesson = ctk.CTkLabel(self.standard_frame, text="", font=("Arial", int(f.get("lesson", 65)), "bold"), text_color=c.get("lesson"), wraplength=800)
        self.lbl_lesson.pack(pady=5)
        self.lbl_timer = ctk.CTkLabel(self.standard_frame, text="00:00", font=("Arial", int(f.get("timer", 300)), "bold"), text_color=c.get("timer"))
        self.lbl_timer.pack()
        self.lbl_ann = ctk.CTkLabel(self.standard_frame, text=self.conf.get("announcement", ""), font=("Arial", int(f.get("announcement", 45)), "italic", "bold"), text_color=c.get("announcement"), wraplength=850)
        self.lbl_ann.pack(expand=True, fill="both")
        self.lbl_clock = ctk.CTkLabel(self.standard_frame, text="", font=("Arial", int(f.get("clock", 120)), "bold"), text_color=c.get("clock"))
        self.lbl_clock.pack(side="bottom", pady=10)

        self.slide_frame = ctk.CTkFrame(self, fg_color="black")
        self.lbl_slide_bg = ctk.CTkLabel(self.slide_frame, text="")
        self.lbl_slide_bg.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        s_size = int(f.get("slide_info", 45))
        t_clr = c.get("slide_info", "#ffffff")
        b_clr = c.get("slide_bg", "#000000")

        # SAYAÇ (Dersin üstünde, Sola Yaslı, 0 Boşluk)
        self.lbl_slide_timer = ctk.CTkLabel(self.slide_frame, text="", font=("Arial", s_size + 15, "bold"), text_color=t_clr, fg_color=b_clr, corner_radius=0)
        self.lbl_slide_timer.place(relx=0.0, rely=0.91, anchor="sw")

        # DERS BİLGİSİ (En Altta, Sola Yaslı, 0 Boşluk)
        self.lbl_slide_lesson = ctk.CTkLabel(self.slide_frame, text="", font=("Arial", s_size, "bold"), text_color=t_clr, fg_color=b_clr, corner_radius=0)
        self.lbl_slide_lesson.place(relx=0.0, rely=1.0, anchor="sw")

    def refresh_slide_images(self):
        self.slide_images = USBManager.get_slide_images()

    def update_info(self, day_text, lesson_text, timer_text, clock_text):
        self.lbl_day.configure(text=day_text)
        self.lbl_lesson.configure(text=lesson_text)
        self.lbl_timer.configure(text=timer_text)
        self.lbl_clock.configure(text=clock_text)

        self.lbl_slide_lesson.configure(text=lesson_text) # Boşluklar kaldırıldı
        self.lbl_slide_timer.configure(text=timer_text) # Boşluklar kaldırıldı
        
        if self.conf.get("slide_active", False):
            if not self.slide_images: self.refresh_slide_images()
            if self.slide_images:
                self.standard_frame.grid_remove()
                self.slide_frame.grid(row=0, column=0, sticky="nsew")
                self.process_slideshow()
        else:
            self.slide_frame.grid_remove()
            self.standard_frame.grid(row=0, column=0, sticky="nsew")

    def process_slideshow(self):
        current_time = time.time()
        interval = int(self.conf.get("slide_interval", 10))
        if current_time - self.last_slide_time >= interval:
            try:
                img_path = self.slide_images[self.current_slide_idx]
                pil_img = Image.open(img_path)
                target_w, target_h = self.slide_frame.winfo_width(), self.slide_frame.winfo_height()
                if target_w < 100: target_w, target_h = 1920, 1080
                fitted_img = ImageOps.fit(pil_img, (target_w, target_h), method=Image.LANCZOS)
                ctk_img = ctk.CTkImage(light_image=fitted_img, dark_image=fitted_img, size=(target_w, target_h))
                self.lbl_slide_bg.configure(image=ctk_img)
                self.current_slide_idx = (self.current_slide_idx + 1) % len(self.slide_images)
                self.last_slide_time = current_time
            except:
                self.current_slide_idx = (self.current_slide_idx + 1) % len(self.slide_images)
