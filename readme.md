
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
