
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
---

## 📖 Kullanım Kılavuzu

### 🎵 Ses ve Melodi Yönetimi
* **Okul Zilleri:** Tüm zil melodileri (Öğrenci, Öğretmen ve Çıkış) `zil/sesler/zilmelodileri/` dizininde tutulur. Uygulama bu dizindeki uygun anonslu dosyaları otomatik olarak kullanır.
* **Marşlar ve Sirenler:** `zil/sesler/marslar/` dizinine eklenen ses dosyaları, **Tören Modu** aktif edildiğinde sol menüde kalıcı bir liste olarak görünür ve hızlı erişim sağlar.

### 💾 USB Bellek ile Medya Yönetimi
Uygulama, takılan USB bellek içerisinde aşağıdaki klasör yapısını otomatik olarak tarar:

| Klasör Adı | İşlev | Çalışma Mantığı |
| :--- | :--- | :--- |
| `muzikyayini` | Teneffüs Müziği | Teneffüs saatlerinde bu dizindeki müzikler sırayla çalınır. |
| `slayt` | Görsel Sunum | Aktif edildiğinde bu dizindeki resimleri sırayla gösterir. |
| `toren` | Etkinlik Dosyaları | Tören esnasında ihtiyaç duyulan özel etkinlik müzikleri. |

#### 🖼️ Slayt Gösterisi
* `slayt` klasörü içindeki görseller (JPG, PNG) sırayla ekrana yansıtılır.
* Geçiş hızı **Ayarlar** sayfasından saniye bazlı olarak değiştirilebilir.

#### 🏛️ Tören Modu
* **Hızlı Erişim:** Sol menüde her zaman `zil/sesler/marslar/` dizinindeki sabit dosyalar listelenir. USB takılıysa `toren` klasöründeki dosyalara da bu mod üzerinden ulaşılabilir.
* **Zil İptali:** Mod aktif olduğu sürece planlanmış tüm ziller otomatik olarak susturulur.

#### ⚠️ ÖNEMLİ: USB Belleği Güvenli Çıkarma
Veri kaybını ve sistem hatalarını önlemek için:
1. Slayt veya müzik yayını devam ediyorsa arayüzden **durdurun**.
2. Fiziksel olarak belleği çekmeden önce uygulamanın aktif olarak dosyayı okumadığından emin olun. Kullanım sırasında çıkarılan bellekler dosya sistemine zarar verebilir.

---
