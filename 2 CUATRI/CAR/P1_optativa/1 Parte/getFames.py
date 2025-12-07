import cv2
from datetime import datetime
import os


os.makedirs("frames", exist_ok=True)

# URL obtenida mediante 'yt-dlp -g'
stream_url = "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1747666307/" \
"ei/I_EqaJiyCu7YxN8P17nemAs/ip/92.190.147.110/id/Rg2QZ5zYukQ.1/itag/96/source/yt_live_broadcast/" \
"requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/" \
"rqh/1/hls_chunk_host/rr2---sn-w511uxa-5ajl.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/playlist_duration/" \
"30/manifest_duration/30/bui/AecWEAYEvh5KPHlHA8ss3lKYQaibJL_p8w9VMNMY0nRFp1zcDjzQe4Av-qVI2_Rwjl79M_ptc0GoGw4E/" \
"spc/wk1kZrf3y4GCYDT6CPz3idg-s9CKiiqrn_Cs40wyBXEmTwAMY92K7K_jfdiR4ALNCGuiATE/vprv/1/playlist_type/DVR/initcwndbps/" \
"3411250/met/1747644708,/mh/aQ/mm/44/mn/sn-w511uxa-5ajl/ms/lva/mv/m/mvi/2/pl/23/rms/lva,lva/dover/11/pacing/0/keepalive/" \
"yes/fexp/51355912,51466698/mt/1747644268/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,rqh,xpc," \
"playlist_duration,manifest_duration,bui,spc,vprv,playlist_type/sig/AJfQdSswRQIgauhbq8hewUnb2CsqHTV-tHuPNNOt5SE7QLTn-" \
"bElnSECIQCUpb-yzNXTzr_Px3ZiGrw_FADo4ZlyV34F3f3Co9pUdg%3D%3D/lsparams/hls_chunk_host,initcwndbps,met,mh,mm,mn,ms,mv,mvi," \
"pl,rms/lsig/ACuhMU0wRQIgGFTMvJ-uZiIobFZdLa46BeZUsxYkb3D_OKU4oJ8Cu2kCIQDjEQpRH3oMj6_49QXEtipltukL68vtsKm3EZFBjSX0Eg%3D%3D" \
"/playlist/index.m3u8" 


cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("No se pudo abrir el stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer un frame.")
        continue
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"frames/frame_{timestamp}.jpg"
    #cv2.imwrite(filename, frame)
    print(f"Guardado: {filename}")
    #time.sleep(random.randint())
