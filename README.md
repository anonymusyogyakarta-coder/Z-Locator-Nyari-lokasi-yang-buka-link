# Z-Locator-Nyari-lokasi-yang-buka-link
<div align="center">

<img src="https://capsule-render.vercel.app/render?type=soft&color=00FF00&height=150&section=header&text=Z-LOCATOR%20TIKTOK&fontSize=50&animation=fadeIn&fontAlignY=35" width="100%" />

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=900&size=35&pause=1000&color=00FF00&center=true&vCenter=true&width=600&lines=PRECISE+GPS+TRACKER;TIKTOK+PRANK+EDITION;RELAX+AJA+BRO!+😎" alt="Typing SVG" />

<p align="center">
  <img src="https://img.shields.io/badge/Developer-Zexr01-00FF00?style=for-the-badge&logo=github&logoColor=black" />
  <img src="https://img.shields.io/badge/Tools-OSINT-00FF00?style=for-the-badge&logo=linux&logoColor=black" />
</p>

---

### 📖 APA ITU Z-LOCATOR?
**Z-Locator** adalah tool OSINT untuk melacak lokasi presisi (GPS) melalui link pancingan bertema TikTok. Cocok digunakan untuk menjebak penipu. Begitu target klik **"Allow/Izinkan"**, koordinat Google Maps mereka akan langsung terkirim ke Termux Anda.

---

### 🛠️ CARA INSTALL & MENJALANKAN (TERMUX)

*Ikuti langkah-langkah di bawah ini secara berurutan:*

**Langkah 1: Persiapan Environment**
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone [https://github.com/anonymusyogyakarta-coder/Z-Locator-TikTok](https://github.com/anonymusyogyakarta-coder/Z-Locator-TikTok)
cd Z-Locator-TikTok
pip install -r requirements.txt
python Z-Locator.py
