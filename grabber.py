import requests
import re
import datetime

def get_live_link(url, regex_pattern):
    """Mencuri pautan m3u8 secara automatik berdasarkan URL dan corak Regex."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Referer': url
        }
        response = requests.get(url, headers=headers, timeout=15)
        match = re.search(regex_pattern, response.text)
        if match:
            return match.group(1).replace('&amp;', '&')
    except:
        pass
    return None

# 1. Header M3U
m3u_content = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. Corak Regex untuk Scraping
# Corak Tonton (TV3, 7, 8, 9)
tonton_reg = r'(https://live-ssar-02\.tonton\.com\.my/[^"\'>]+\.m3u8[^"\'>]*)'
# Corak Mana2 (TVS, Bernama, Alhijrah)
mana2_reg = r'(https://live\.mana2\.my/[^"\'>]+\.m3u8[^"\'>]*)'

# 3. SENARAI SALURAN (Susunan Wajib Anda)
channels = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1", "Tv1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2", "Tv2"),
    ("TV3", get_live_link("https://www.tonton.com.my/live-tv/tv3", tonton_reg), "https://www.tonton.com.my/", "TV3", "Tv3"),
    ("TV Alhijrah", get_live_link("https://www.mana2.my/live/tv-alhijrah", mana2_reg), "https://www.mana2.my/", "TVAlhijrah", "TvAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY", "OkeyTv"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6", "Tv6"),
    ("DidikTV KPM", get_live_link("https://www.tonton.com.my/live-tv/ntv7", tonton_reg), "https://www.tonton.com.my/", "DidikTVKPM", "DidikTv"),
    ("8TV", get_live_link("https://www.tonton.com.my/live-tv/8tv", tonton_reg), "https://www.tonton.com.my/", "8TV", "8tv"),
    ("TV9", get_live_link("https://www.tonton.com.my/live-tv/tv9", tonton_reg), "https://www.tonton.com.my/", "TV9", "Tv9"),
    ("TVS", get_live_link("https://www.mana2.my/live/tvs", mana2_reg), "https://www.mana2.my/", "TVS", "Tvs"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani", "AstroAwani"),
    ("BERITA RTM", "https://mifntechnology.github.io/siaranMy/channels/BeritaRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "BERITARTM", "BeritaRtm"),
    ("SUKAN RTM", "https://mifntechnology.github.io/siaranMy/channels/SukanRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "TVSUKAN", "SukanRtm"),
    ("Bernama TV", get_live_link("https://www.mana2.my/live/bernama-tv", mana2_reg), "https://www.mana2.my/", "BernamaTV", "Bernama")
]

# 4. SENARAI RADIO (Penuh 13)
radio_list = [
    ("Hot Fm", "HotFm", "Hot FM", "HotFm"), ("Best Fm", "BestFm", "Best FM", "bestfm"),
    ("Kool 101", "BuletinFm", "Kool FM", "Kool101"), ("Era", "Era", "ERA", "Era"),
    ("Fly Fm", "FlyFm", "Fly FM", "FlyFm"), ("Hitz Fm", "HitzFm", "Hitz FM", "HitzFm"),
    ("Johor Fm", "JohorFm", "Johor FM", "JohorFm"), ("NasionalFm", "NasionalFm", "NASFM", "NasionalFm"),
    ("Radio Klasik", "RadioKlasik", "Klasik FM", "RadioKlasik"), ("SinarFm", "SinarFm", "Sinar FM", "SinarFm"),
    ("SuriaFm", "SuriaFm", "Suria FM", "Suria"), ("Ria897Fm", "RiaFm", "Ria FM", "RiaFm"),
    ("AsyikFm", "AsyikFm", "Asyik FM", "AsyikFm")
]

# Proses Penulisan TV
for name, url, ref, tvgid, logo in channels:
    if url:
        m3u_content += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\n'
        m3u_content += f'#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

# Proses Penulisan Radio
for name, folder, tvgid, logo in radio_list:
    m3u_content += f'#EXTINF:-1 group-title="radio" tvg-id="{tvgid}" tvg-name="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\nhttps://mifntechnology.github.io/siaranMy/radio/{folder}/playlist.m3u8\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
