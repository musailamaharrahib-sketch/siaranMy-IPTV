import requests
import re
import datetime

def get_live_link(target_url, regex_pattern):
    """Mencuri pautan m3u8 secara automatik melalui jambatan proxy."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'X-Forwarded-For': '210.186.111.1' # IP Unifi Malaysia
    }
    try:
        # Gunakan AllOrigins sebagai jambatan untuk tembus geo-block
        proxy_bridge = f"https://api.allorigins.win/get?url={requests.utils.quote(target_url)}"
        response = requests.get(proxy_bridge, timeout=20)
        data = response.json()
        html = data['contents']
        
        match = re.search(regex_pattern, html)
        if match:
            return match.group(1).replace('&amp;', '&')
    except:
        pass
    return None

# 1. Header M3U
m3u_header = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. Corak Regex
tonton_reg = r'(https://live-ssar-02\.tonton\.com\.my/[^"\'>]+\.m3u8[^"\'>]*)'
mana2_reg = r'(https://live\.mana2\.my/[^"\'>]+\.m3u8[^"\'>]*)'

# 3. SENARAI SALURAN (Ikut Susunan Wajib Anda)
channels_config = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2"),
    ("TV3", get_live_link("https://www.tonton.com.my/live-tv/tv3", tonton_reg), "https://www.tonton.com.my/", "TV3"),
    ("TV Alhijrah", get_live_link("https://www.mana2.my/live/tv-alhijrah", mana2_reg), "https://www.mana2.my/", "TVAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6"),
    ("DidikTV KPM", get_live_link("https://www.tonton.com.my/live-tv/ntv7", tonton_reg), "https://www.tonton.com.my/", "DidikTVKPM"),
    ("8TV", get_live_link("https://www.tonton.com.my/live-tv/8tv", tonton_reg), "https://www.tonton.com.my/", "8TV"),
    ("TV9", get_live_link("https://www.tonton.com.my/live-tv/tv9", tonton_reg), "https://www.tonton.com.my/", "TV9"),
    ("TVS", get_live_link("https://www.mana2.my/live/tvs", mana2_reg), "https://www.mana2.my/", "TVS"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani")
]

# 4. SENARAI RADIO (Penuh 13)
radio_list = [
    ("Hot Fm", "HotFm", "HotFm"), ("Best Fm", "BestFm", "bestfm"),
    ("Kool 101", "BuletinFm", "Kool101"), ("Era", "Era", "Era"),
    ("Fly Fm", "FlyFm", "FlyFm"), ("Hitz Fm", "HitzFm", "HitzFm"),
    ("Johor Fm", "JohorFm", "JohorFm"), ("NasionalFm", "NasionalFm", "NasionalFm"),
    ("Radio Klasik", "RadioKlasik", "RadioKlasik"), ("SinarFm", "SinarFm", "SinarFm"),
    ("SuriaFm", "SuriaFm", "Suria"), ("Ria897Fm", "RiaFm", "RiaFm"),
    ("AsyikFm", "AsyikFm", "AsyikFm")
]

# Bina Kandungan Fail
full_m3u = m3u_header

for name, url, ref, tvgid in channels_config:
    if not url: # Jika scrap gagal, guna backup github.io
        url = f"https://mifntechnology.github.io/siaranMy/channels/{tvgid}/index.m3u8"
        
    logo = f"https://mifntechnology.github.io/siaranMy/logo/{tvgid}.png"
    full_m3u += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="{logo}",{name}\n'
    full_m3u += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\n'
    full_m3u += f'#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

for name, folder, logo in radio_list:
    full_m3u += f'#EXTINF:-1 group-title="radio" tvg-id="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\nhttps://mifntechnology.github.io/siaranMy/radio/{folder}/playlist.m3u8\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(full_m3u)
