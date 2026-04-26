import customtkinter as ctk
import datetime
import os

class ZamanAyarla(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Saat ve Tarih Ayarı")
        self.geometry("600x350")
        self.eval('tk::PlaceWindow . center')
        
        ctk.CTkLabel(self, text="SİSTEM SAATİNİ AYARLA", font=("Arial", 24, "bold")).pack(pady=30)
        
        f = ctk.CTkFrame(self, fg_color="transparent")
        f.pack(pady=10)
        
        now = datetime.datetime.now()
        
        self.ent_d = ctk.CTkEntry(f, width=70, height=50, font=("Arial", 20), justify="center")
        self.ent_d.insert(0, now.strftime("%d"))
        self.ent_d.grid(row=0, column=0, padx=5)
        
        ctk.CTkLabel(f, text="/", font=("Arial", 24)).grid(row=0, column=1)
        
        self.ent_m = ctk.CTkEntry(f, width=70, height=50, font=("Arial", 20), justify="center")
        self.ent_m.insert(0, now.strftime("%m"))
        self.ent_m.grid(row=0, column=2, padx=5)
        
        ctk.CTkLabel(f, text="/", font=("Arial", 24)).grid(row=0, column=3)
        
        self.ent_y = ctk.CTkEntry(f, width=100, height=50, font=("Arial", 20), justify="center")
        self.ent_y.insert(0, now.strftime("%Y"))
        self.ent_y.grid(row=0, column=4, padx=5)
        
        ctk.CTkLabel(f, text="   -   ", font=("Arial", 24)).grid(row=0, column=5)
        
        self.ent_h = ctk.CTkEntry(f, width=70, height=50, font=("Arial", 20), justify="center")
        self.ent_h.insert(0, now.strftime("%H"))
        self.ent_h.grid(row=0, column=6, padx=5)
        
        ctk.CTkLabel(f, text=":", font=("Arial", 24)).grid(row=0, column=7)
        
        self.ent_min = ctk.CTkEntry(f, width=70, height=50, font=("Arial", 20), justify="center")
        self.ent_min.insert(0, now.strftime("%M"))
        self.ent_min.grid(row=0, column=8, padx=5)
        
        self.btn = ctk.CTkButton(self, text="KAYDET VE ÇIK", fg_color="#e67e22", width=250, height=60, font=("Arial", 20, "bold"), command=self.kaydet)
        self.btn.pack(pady=40)

    def kaydet(self):
        try:
            d = self.ent_d.get().zfill(2)
            m = self.ent_m.get().zfill(2)
            y = self.ent_y.get()
            h = self.ent_h.get().zfill(2)
            min_ = self.ent_min.get().zfill(2)
            
            new_date = f"{y}-{m}-{d} {h}:{min_}:00"
            os.system("sudo -n timedatectl set-ntp false")
            os.system(f'sudo -n timedatectl set-time "{new_date}"')
            
            self.btn.configure(text="BAŞARILI!", fg_color="#2ecc71")
            self.after(1500, self.destroy)
        except: 
            pass

if __name__ == "__main__":
    app = ZamanAyarla()
    app.mainloop()
