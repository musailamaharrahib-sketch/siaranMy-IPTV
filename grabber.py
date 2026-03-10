import requests
import re
import datetime

def get_tonton_link(channel_id):
    """Mengambil pautan m3u8 terbaru daripada Tonton dengan Header yang lebih kuat."""
    try:
        url = f"https://www.tonton.com.my/live-tv/{channel_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Referer': 'https://www.tonton.com.my/',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response = requests.get(url, headers=headers, timeout=20)
        
        # Mencari pautan master.m3u8 berserta token panjang
        # Regex ini mencari pautan yang bermula dengan https dan mengandungi master.m3u8
        match = re.search(r'(https://live-ssar-02\.tonton\.com\.my/[^\s"\'<>]+master\.m3u8\?[^\s"\'<>]+)', response.text)
        
        if match:
            return match.group(1)
        return None
    except Exception as e:
        print(f"Ralat pada {channel_id}: {e}")
        return None

# --- Kod seterusnya (Header M3U & Proses Saluran) kekalkan seperti yang saya beri sebelum ini ---
