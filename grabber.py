import requests
import re
import datetime

def get_tonton_link(channel_id, manual_link):
    """Mencuri token Tonton. Jika gagal, guna pautan manual anda."""
    try:
        url = f"https://www.tonton.com.my/live-tv/{channel_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
            'Referer': 'https://www.tonton.com.my/'
        }
        response = requests.get(url, headers=headers, timeout=15)
        match = re.search(r'(https://live-ssar-02\.tonton\.com\.my/[^"\'>]+\.m3u8[^"\'>]*)', response.text)
        if match:
            return match.group(1).replace('&amp;', '&')
    except:
        pass
    return manual_link # Gunakan pautan yang anda beri jika robot gagal

# Pautan manual anda (Sebagai backup)
tv9_backup = "https://live-ssar-02.tonton.com.my/1773137950/bd28ffb014fa282c68db6f60fabec89dc8a64edf69f48c293a34758889950fc1/tv9/master.m3u8?bpkio_serviceid=6c0958d82a830a026ba9f8eeb79ede62&did=79b00b12-6a77-4424-5e76-2ced2d51e1ec&dnt=0&ifatype=sessionid&plt=web&lot_auds=&ttd_uid2=A4AAACx19Cup1dLf_pFtbHX1acGf13TYVWAVBcsIMaHgTbodVuMf5Lm43m0O3iDkk7XkkjcET_BQJV2D8mGQxi-GZRKdgZ-SRb-qVU1o0AiLvKMqUhcNbnY5ETKN_x31Sm1MneG2BLx3HBhXAfnyYaAVkS4DaceUAEyajynsw2jiD0jvI8_Jc7Zn6pEuZGjTAx1OqpAJa8J7EHHGa2uencSdQA&bpkio_sessionid=10f3b5b25-4d46b1cc-3b25-4ce4-b352-67f739876fef&category=all"

# 1. Header M3U
m3u_content = '#EXTM3U x-tvg-url="https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml" url-tvg="https://raw.githubusercontent.com/AqFad2811/epg/main/compressed/epg.xml.gz" refresh="1440" max-conn="1"\n\n'

# 2. Ambil token Tonton
tv3_link = get_tonton_link("tv3", "https://mifntechnology.github.io/siaranMy/channels/Tv3/index.m3u8")
tv9_link = get_tonton_link("tv9", tv9_backup)

# 3. Susunan Saluran
channels = [
    ("TV1", "https://mifntechnology.github.io/siaranMy/channels/Tv1/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV1", "Tv1"),
    ("TV2", "https://mifntechnology.github.io/siaranMy/channels/Tv2/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV2", "Tv2"),
    ("TV3", tv3_link, "https://www.tonton.com.my/", "TV3", "Tv3"),
    ("TV Alhijrah", "https://live.mana2.my/TvAlhijrah/index.m3u8", "https://www.mana2.my/", "TVAlhijrah", "TvAlhijrah"),
    ("Okey TV", "https://mifntechnology.github.io/siaranMy/channels/TvOkey/index.m3u8", "https://rtmklik.rtm.gov.my/", "OKEY", "OkeyTv"),
    ("TV6", "https://mifntechnology.github.io/siaranMy/channels/Tv6/index.m3u8", "https://rtmklik.rtm.gov.my/", "TV6", "Tv6"),
    ("TV9", tv9_link, "https://www.tonton.com.my/", "TV9", "Tv9"),
    ("TVS", "https://live.mana2.my/TvS/index.m3u8", "https://www.mana2.my/", "TVS", "Tvs"),
    ("Astro Awani", "https://mifntechnology.github.io/siaranMy/channels/AstroAwani/index.m3u8", "https://www.astroawani.com/", "AstroAwani", "AstroAwani")
]

# (Tambah Radio anda di sini seperti biasa)
radio_list = [("Hot Fm", "HotFm", "Hot FM", "HotFm"), ("NasionalFm", "NasionalFm", "NASFM", "NasionalFm")]

# Penulisan fail
for name, url, ref, tvgid, logo in channels:
    m3u_content += f'#EXTINF:-1 group-title="siaranMy" tvg-id="{tvgid}" tvg-name="{tvgid}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\n'
    m3u_content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer={ref}\n{url}\n\n'

for name, folder, tvgid, logo in radio_list:
    m3u_content += f'#EXTINF:-1 group-title="radio" tvg-id="{tvgid}" tvg-name="{name}" tvg-logo="https://mifntechnology.github.io/siaranMy/logo/{logo}.png",{name}\nhttps://mifntechnology.github.io/siaranMy/radio/{folder}/playlist.m3u8\n\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
