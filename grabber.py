import requests
import re
import datetime

def get_tonton_link(channel_id):
    """Mencuba mencuri pautan, jika gagal pulangkan None."""
    try:
        url = f"https://www.tonton.com.my/live-tv/{channel_id}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'(https://live-ssar-02\.tonton\.com\.my/[^"\'>]+\.m3u8[^"\'>]*)', response.text)
        if match:
            return match.group(1).replace('&amp;', '&')
    except:
        pass
    return None

# 1. Header M3U
m3u_content = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. Ambil token Tonton
tonton_ids = {"TV3": "tv3", "DidikTVKPM": "ntv7", "8TV": "8tv", "TV9": "tv9"}
tonton_results = {}
for name, webid in tonton_ids.items():
    link = get_tonton_link(webid)
    # JIKA SCRAPING GAGAL, GUNA PAUTAN ALTERNATIF (PROXY)
    if not link:
        if webid == "tv3": link = "https://tonton-live.akamaized.net/hls/live/2043564/tv3/master.m3u8"
        elif webid == "ntv7": link = "https://tonton-live.akamaized.net/hls/live/2043565/ntv7/master.m3u8"
        elif webid == "8tv": link = "https://tonton-live.akamaized.net/hls/live/2043566/8tv/master.m3u8"
        elif webid == "tv9": link = "https://tonton-live.akamaized.net/hls/live/2043567/tv9/master.m3u8"
    tonton_results[name] = link

# 3. Susunan Saluran Utama (Kekal ikut permintaan anda)
main_tv = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1", "Tv1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2", "Tv2"),
    ("TV3", tonton_results.get("TV3"), "https://www.tonton.com.my/", "TV3", "Tv3"),
    ("TV Alhijrah", "https://live.mana2.my/TvAlhijrah/index.m3u8?auth_key=1773131819-45746f7d57b74f7da995f797a26668f3-0-2a031436c448dbaf06341eeb793ad26c", "https://www.mana2.my/", "TVAlhijrah", "TvAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY", "OkeyTv"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6", "Tv6"),
    ("DidikTV KPM", tonton_results.get("DidikTVKPM"), "https://www.tonton.com.my/", "DidikTVKPM", "DidikTv"),
    ("8TV", tonton_results.get("8TV"), "https://www.tonton.com.my/", "8TV", "8tv"),
    ("TV9", tonton_results.get("TV9"), "https://www.tonton.com.my/", "TV9", "Tv9"),
    ("TVS", "https://live.mana2.my/TvS/index.m3u8?auth_key=1773142589-d03dd30fb97d41bc9dc65d914d51013d-0-b25ce1dc03899973abd33fdb44577535", "https://www.mana2.my/", "TVS", "Tvs"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani", "AstroAwani")
]

# Tambah EXTRA TV
extra_tv = [
    ("BERITA RTM", "https://mifntechnology.github.io/siaranMy/channels/BeritaRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "BERITARTM", "BeritaRtm"),
    ("SUKAN RTM", "https://mifntechnology.github.io/siaranMy/channels/SukanRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "TVSUKAN", "SukanRtm"),
    ("Bernama TV", "https://live.mana2.my/Bernama/index.m3u8?auth_key=1773142810-7e2c584028ce43f385da750b46bc4612-0-1153ee8a86d054b7174eda2d0975bec7", "https://www.mana2.my/", "BernamaTV", "Bernama")
]

# Radio (13 Saluran)
radio_list = [
    ("Hot Fm", "HotFm", "Hot FM", "HotFm"), ("Best Fm", "BestFm", "Best FM", "bestfm"),
    ("Kool 101", "BuletinFm", "Kool FM", "Kool101"), ("Era", "Era", "ERA", "Era"),
    ("Fly Fm", "FlyFm", "Fly FM", "FlyFm"), ("Hitz Fm", "HitzFm", "Hitz FM", "HitzFm"),
    ("Johor Fm", "JohorFm", "Johor FM", "JohorFm"), ("NasionalFm", "NasionalFm", "NASFM", "NasionalFm"),
    ("Radio Klasik", "RadioKlasik", "Klasik FM", "RadioKlasik"), ("SinarFm", "SinarFm", "Sinar FM", "SinarFm"),
    ("SuriaFm", "SuriaFm", "Suria FM", "Suria"), ("Ria897Fm", "RiaFm", "Ria FM", "RiaFm"),
    ("AsyikFm", "AsyikFm", "Asyik FM", "AsyikFm")
]

# Proses Penulisan
for name, url, ref, tvgid, logo in (main_tv + extra_tv):
    if url:
        m3u_content += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\n'
        m3u_content += f'#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

for name, folder, tvgid, logo in radio_list:
    m3u_content += f'#EXTINF:-1 group-title="radio" tvg-id="{tvgid}" tvg-name="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\nhttps://mifntechnology.github.io/siaranMy/radio/{folder}/playlist.m3u8\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
