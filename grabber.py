import requests
import re
import datetime

def get_tonton_link(channel_id):
    """Mencuri pautan master.m3u8 terbaru daripada Tonton secara automatik."""
    try:
        url = f"https://www.tonton.com.my/live-tv/{channel_id}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        match = re.search(r'https://live-ssar-02\.tonton\.com\.my/[^\s"]+master\.m3u8\?[^\s"]+', response.text)
        return match.group(0) if match else None
    except: return None

# 1. Header M3U (EPG)
m3u_content = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. Ambil token Tonton Auto
tonton_links = {"tv3": get_tonton_link("tv3"), "ntv7": get_tonton_link("ntv7"), "8tv": get_tonton_link("8tv"), "tv9": get_tonton_link("tv9")}

# 3. SENARAI TV (Susunan Wajib Anda)
main_tv = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1", "Tv1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2", "Tv2"),
    ("TV3", tonton_links["tv3"], "https://www.tonton.com.my/", "TV3", "Tv3"),
    ("TV Alhijrah", "https://live.mana2.my/TvAlhijrah/index.m3u8?auth_key=1773131819-45746f7d57b74f7da995f797a26668f3-0-2a031436c448dbaf06341eeb793ad26c", "https://www.mana2.my/", "TVAlhijrah", "TvAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY", "OkeyTv"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6", "Tv6"),
    ("DidikTV KPM", tonton_links["ntv7"], "https://www.tonton.com.my/", "DidikTVKPM", "DidikTv"),
    ("8TV", tonton_links["8tv"], "https://www.tonton.com.my/", "8TV", "8tv"),
    ("TV9", tonton_links["tv9"], "https://www.tonton.com.my/", "TV9", "Tv9"),
    ("TVS", "https://live.mana2.my/TvS/index.m3u8?auth_key=1773142589-d03dd30fb97d41bc9dc65d914d51013d-0-b25ce1dc03899973abd33fdb44577535", "https://www.mana2.my/", "TVS", "Tvs"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani", "AstroAwani")
]

# 4. SENARAI RADIO (13 Saluran)
radio_channels = [
    ("Hot Fm", "HotFm/playlist.m3u8", "Hot FM", "HotFm"), ("Best Fm", "BestFm/playlist.m3u8", "Best FM", "bestfm"),
    ("Kool 101", "BuletinFm/playlist.m3u8", "Kool FM", "Kool101"), ("Era", "Era/playlist.m3u8", "ERA", "Era"),
    ("Fly Fm", "FlyFm/playlist.m3u8", "Fly FM", "FlyFm"), ("Hitz Fm", "HitzFm/playlist.m3u8", "Hitz FM", "HitzFm"),
    ("Johor Fm", "JohorFm/playlist.m3u8", "Johor FM", "JohorFm"), ("NasionalFm", "NasionalFm/playlist.m3u8", "NASFM", "NasionalFm"),
    ("Radio Klasik", "RadioKlasik/playlist.m3u8", "Klasik FM", "RadioKlasik"), ("SinarFm", "SinarFm/playlist.m3u8", "Sinar FM", "SinarFm"),
    ("SuriaFm", "SuriaFm/playlist.m3u8", "Suria FM", "Suria"), ("Ria897Fm", "RiaFm/playlist.m3u8", "Ria FM", "RiaFm"),
    ("AsyikFm", "AsyikFm/playlist.m3u8", "Asyik FM", "AsyikFm")
]

# Proses TV
for name, url, ref, tvgid, logo in main_tv:
    if url:
        m3u_content += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\n'
        m3u_content += f'#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

# Proses Radio
for name, folder, tvgid, logo in radio_channels:
    url = f"https://mifntechnology.github.io/siaranMy/radio/{folder}"
    m3u_content += f'#EXTINF:-1 group-title="radio" tvg-id="{tvgid}" tvg-name="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n{url}\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f: f.write(m3u_content)
