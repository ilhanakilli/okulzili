
# 🔔 OkulZili Uygulaması

Bu proje; Raspberry Pi 5, Linux Mint ve Ubuntu tabanlı sistemler için geliştirilmiş, Python ve CustomTkinter altyapısını kullanan profesyonel bir okul zili otomasyonudur. 

## 🚀 Kurulum Adımları

Kurulumu sıfırdan yapmak için terminali açın ve aşağıdaki blokları sırasıyla kopyalayıp yapıştırın.

### 1. Dosyaları İndirme ve Hazırlık
Proje dosyalarını çekiyoruz ve başlatıcı simgelerini masaüstüne taşıyoruz.

```bash
cd $(xdg-user-dir DESKTOP)
git clone https://github.com/ilhanakilli/okulzili.git zil
cd zil
mv *.desktop ..
chmod +x *.sh
```

### 2. Sistem Gereksinimlerinin Kurulması
Uygulamanın çalışması için gerekli olan Python, Pip ve Medya (VLC) kütüphanelerini sisteme yüklüyoruz.

```bash
sudo apt update
sudo apt install python3-venv python3-pip python3-tk vlc libvlc-dev -y
```

### 3. Python Sanal Ortamı (venv) ve Kütüphaneler
Bağımlılıkların sistemden izole çalışması için sanal ortamı hazırlıyoruz.

```bash
python3 -m venv venv
source venv/bin/activate
pip install customtkinter pillow python-vlc
```

### 4. Zaman Ayarı Yetkilendirmesi (Önemli)
Uygulama üzerinden sistem saatinin güncellenebilmesi için şu komutu çalıştırarak gerekli izni tanımlayın:

```bash
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/timedatectl" | sudo tee /etc/sudoers.d/timedatectl
```

## 🛠 Kullanım ve Başlatma

- **Simgeleri Aktifleştirme:** Masaüstüne gelen Okul Zili ve Zaman Ayarla simgelerine sağ tıklayıp "Allow Launching" (Başlatmaya İzin Ver) seçeneğine tıklayın.
- **Uygulamayı Başlatma:** Masaüstündeki simgelere çift tıklayarak sistemi kullanmaya başlayabilirsiniz.
- **İçerik Yönetimi:** Müzik ve slayt görsellerini zil klasörü içindeki ilgili dizinlere ekleyebilir veya USB bellek üzerinden otomatik oynatabilirsiniz.

## 📋 Teknik Özellikler

- **Arayüz:** CustomTkinter (Modern GUI)
- **Ses Motoru:** VLC Lib (Yüksek kaliteli ses işleme)
- **Uyumluluk:** Raspberry Pi 5 (Wayland/PipeWire destekli) ve Linux Dağıtımları

- ## 🕒 Sistem Açılışında Otomatik Başlatma

Uygulamanın bilgisayar açıldığında otomatik olarak devreye girmesi için aşağıdaki adımları uygulayın. Bu yöntem hem **Linux Mint (XFCE)** hem de **Raspberry Pi 5** ile tam uyumludur.

### 🛠 Otomatik Başlatıcıyı Oluşturma
Terminali açın ve aşağıdaki komut bloğunu olduğu gibi kopyalayıp yapıştırın. Bu komut, sistem diliniz ne olursa olsun Masaüstü dizininizi bulur ve gerekli başlatıcıyı sisteme kaydeder:

```bash
mkdir -p ~/.config/autostart
cat <<EOF > ~/.config/autostart/okulzili.desktop
[Desktop Entry]
Type=Application
Name=Okul Zili Otomatik Başlatıcı
Comment=Sistem açılışında okul zilini başlatır
Exec=sh -c 'cd "\$(xdg-user-dir DESKTOP)/zil" && chmod +x otostart.sh && ./otostart.sh'
Terminal=false
X-GNOME-Autostart-enabled=true
EOF
```
💡 Alternatif Yöntem (Arayüz ile)
Eğer komut kullanmak istemiyorsanız:

Ayarlar > Oturum ve Başlangıç > Uygulama Otomatik Başlat sekmesine gidin.

Ekle butonuna tıklayın.

Komut (Command) kısmına aşağıdakini yapıştırın:

```Bash
sh -c 'cd "$(xdg-user-dir DESKTOP)/zil" && ./otostart.sh'
```
⚠️ Önemli Hatırlatmalar
Gecikme: otostart.sh içerisinde varsayılan olarak 5 saniye bekleme (sleep 5) tanımlıdır. Bu, sistemin ses ve görüntü sürücülerinin tam yüklenmesini sağlar.

İzinler: Eğer uygulama açılmazsa, terminalden şu komutla izinleri tazeleyin:

```Bash
chmod +x $(xdg-user-dir DESKTOP)/zil/otostart.sh
```
## 📖 Kullanım Kılavuzu

### ⏰ Saat ve Program Ayarları
* **Ders Kapasitesi:** Günlük **15 saate kadar** ders girişi yapılabilir.
* **Öğle Arası:** Tanımlanan teneffüsler arasından istenilen saat "Öğle Arası" olarak işaretlenebilir ve ekranda bu şekilde belirtilir.
* **Esnek Takvim:** Zil saatleri **gün bazlı** (her güne ayrı) veya **haftalık** (tüm hafta aynı) olarak atanabilir.

### 🖥️ Ana Panel ve Sistem Takibi
Ana pano, sistemin durumu hakkında anlık bilgi sunan bir kontrol merkezidir:

* **Merkezi Sayaç:** Bir sonraki zilin çalmasına kalan süre ana odak olarak saniye saniye geri sayar.
* **Bilgi Ekranı:** O anki ders bilgisi, güncel tarih ve saat bilgisi sürekli takip edilebilir.
* **Yan Panel (Hızlı Erişim):** Sistem yönetimi için şu butonlar yer alır:
    * **Siren:** Acil durumlar için anlık yüksek sesli siren tetikleyici.
    * **Tören Modu:** Özel etkinlikler için zil sistemini askıya alan mod.
    * **Ayarlar:** Sistem yapılandırma sayfasına hızlı geçiş.
    * **Mod Anahtarları:** Slayt Gösterisi ve Müzik Yayını için bağımsız Aktif/Pasif butonları.
    * **Zil Sistemi:** Tüm zil programını tek tuşla pasif veya aktif hale getirme.
    * **Ses Kontrolü:** Sistem ana ses seviyesi için slider (kaydırıcı) ayarı.
    * **USB Güvenli Çıkar:** Belleği yazılımsal olarak ayırma butonu.

### 🎵 Ses ve Melodi Yönetimi
* **Okul Zilleri:** Tüm zil melodileri `zil/sesler/zilmelodileri/` dizininde tutulur. Uygulama bu dizindeki anonslu dosyaları otomatik eşleştirir.
* **Marşlar ve Sirenler:** `zil/sesler/marslar/` dizinine eklenen sesler, **Tören Modu** aktif edildiğinde sol menüde kalıcı bir liste olarak görünür.

### 💾 USB Bellek ile Medya Yönetimi
Uygulama, takılan USB içerisindeki şu klasör yapısını otomatik tarar:

| Klasör Adı | İşlev | Çalışma Mantığı |
| :--- | :--- | :--- |
| `muzikyayini` | Teneffüs Müziği | Teneffüs saatlerinde bu dizindeki müzikler sırayla çalınır. |
| `slayt` | Görsel Sunum | Aktif edildiğinde bu dizindeki resimleri sırayla gösterir. |
| `toren` | Etkinlik Dosyaları | Tören modunda erişilebilen özel etkinlik müzikleri. |

#### 🖼️ Slayt Gösterisi
* `slayt` klasörü içindeki görseller (JPG, PNG) sırayla yansıtılır.
* Geçiş hızı **Ayarlar** sayfasından saniye bazlı değiştirilebilir.

#### 🏛️ Tören Modu
* **Hızlı Erişim:** Sol menüde her zaman `zil/sesler/marslar/` dizinindeki sabit dosyalar listelenir. USB takılıysa `toren` klasöründeki dosyalara da bu panelden ulaşılabilir.
* **Zil İptali:** Mod aktif olduğu sürece planlanmış tüm ziller otomatik olarak susturulur.

#### ⚠️ ÖNEMLİ: USB Belleği Güvenli Çıkarma
Veri kaybını ve sistem donmalarını önlemek için:
1. Slayt gösterisi veya müzik yayını devam ediyorsa yan panelden **durdurun**.
2. Fiziksel olarak belleği çekmeden önce yan paneldeki **"USB'yi Güvenli Çıkar"** butonuna basın.

### 🖥️ Ekran ve Çözünürlük
* **Optimize Edilen Çözünürlük:** Uygulama arayüzü **1080p (1920x1080)** standartlarına göre tasarlanmıştır.
  
###🔄 Otomatik Bakım (Zamanlanmış Yeniden Başlatma)
Sistemin uzun süreli açık kalması durumunda ses sürücülerinin (Pipewire/PulseAudio) kilitlenmesini önlemek ve belleği temizlemek için her sabah 07:00'de otomatik yeniden başlatma yapılması önerilir.

Terminali açın ve aşağıdaki komutu yapıştırarak bu işlemi tek seferde sisteme kaydedin:

```Bash
(sudo crontab -l 2>/dev/null; echo "00 07 * * * /sbin/reboot") | sudo crontab -
```
Alternatif (Manuel) Yöntem:
Komut çalışmazsa veya elle kontrol etmek isterseniz:

Terminale 
```Bash
sudo crontab -e yazın.
```
Açılan dosyanın en altına şu satırı ekleyin:

```Bash
00 07 * * * /sbin/reboot
```
Dosyayı kaydedip çıkın (CTRL+O, Enter, CTRL+X).

💡 Not: Bu işlemden sonra sistem her sabah 07:00'de yeniden başlayacak ve saat 09:00'a kadar ders bilgisi panelinde sizi "Günaydın" mesajı ile karşılayacaktır.

Bu komut tam olarak ne yapıyor?
sudo crontab -l: Mevcut zamanlanmış görevlerini listeler.

echo "00 07 * * * /sbin/reboot": "Her gün saat 07:00'de reboot at" kuralını hazırlar.

| sudo crontab -: Bu kuralı mevcut listenin sonuna ekleyip sisteme geri yükler.
