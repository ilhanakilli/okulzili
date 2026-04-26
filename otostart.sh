#!/bin/bash
# Masaüstünün ve ses servislerinin yüklenmesi için bekle
sleep 5

# GUI için ekran tanımlamaları (Hangi kullanıcı olursa olsun çalışır)
export DISPLAY=:0
export WAYLAND_DISPLAY=wayland-0

# Scriptin o an bulunduğu klasörü otomatik tespit et ve oraya git
cd "$(dirname "$0")"

# Sanal ortamı (venv) mevcut dizine göre çalıştır
./venv/bin/python3 main.py
