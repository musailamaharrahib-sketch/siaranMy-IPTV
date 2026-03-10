import datetime

# 1. Header M3U
m3u_content = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. SENARAI TV (Susunan Wajib Anda)
# Kita guna pautan akamaized yang disertakan User-Agent khusus supaya tidak mati
channels = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1", "Tv1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2", "Tv2"),
    ("TV3", "https://tonton-live.akamaized.net/hls/live/2043564/tv3/master.m3u8", "https://www.tonton.com.my/", "TV3", "Tv3"),
    ("TV Alhijrah", "https://live.mana2.my/TvAlhijrah/index.m3u8", "https://www.mana2.my/", "TVAlhijrah", "TvAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY", "OkeyTv"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6", "Tv6"),
    ("DidikTV KPM", "https://tonton-live.akamaized.net/hls/live/2043565/ntv7/master.m3u8", "https://www.tonton.com.my/", "DidikTVKPM", "DidikTv"),
    ("8TV", "https://tonton-live.akamaized.net/hls/live/2043566/8tv/master.m3u8", "https://www.tonton.com.my/", "8TV", "8tv"),
    ("TV9", "https://tonton-live.akamaized.net/hls/live/2043567/tv9/master.m3u8", "https://www.tonton.com.my/", "TV9", "Tv9"),
    ("TVS", "https://tvslive.akamaized.net/hls/live/2042785/tvs/master.m3u8", "https://www.rtmklik.rtm.gov.my/", "TVS", "Tvs"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani", "AstroAwani"),
    ("BERITA RTM", "https://mifntechnology.github.io/siaranMy/channels/BeritaRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "BERITARTM", "BeritaRtm"),
    ("SUKAN RTM", "https://mifntechnology.github.io/siaranMy/channels/SukanRTM/index.m3u8", "https://rtmklik.rtm.gov.my/", "TVSUKAN", "SukanRtm"),
    ("Bernama TV", "https://rtm-live.akamaized.net/hls/live/2022312/bernama/master.m3u8", "https://www.rtmklik.rtm.gov.my/", "BernamaTV", "Bernama")
]

# 3. SENARAI RADIO (Penuh 13)
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
    m3u_content += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n'
    m3u_content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\n'
    m3u_content += f'#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

# Proses Penulisan Radio
for name, folder, tvgid, logo in radio_list:
    m3u_content += f'#EXTINF:-1 group-title="radio" tvg-id="{tvgid}" tvg-name="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\nhttps://mifntechnology.github.io/siaranMy/radio/{folder}/playlist.m3u8\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
