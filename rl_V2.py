#!/usr/bin/env python3

##########################################################
#                   ATENÇÃO                              #   
# O script e uma coisa nova pois ainda não exister       #
# por isso ele vai ter novas versões com tempo, essa     #
# ideia partir de uma incianter de programação em python #
# em alguns videos não poder dá certo, por contra do     #
# arquivo srt, que poder não está dercondo com tempo     # 
# video passando...                                      #
########################################################## 


from __future__ import print_function # função de prints 
from datetime import datetime, timezone, timedelta # hora e data, nomomento da modificação do video orginal
from tools.bannrs import blue_bannes, write_bannes # print de boas vindas do programa
from tools.audio_tunneling import Tunneling_voice # juntar todos os audios criandos
from pydub.utils import mediainfo # extrair o time do video em segundos
from moviepy.editor import * # extrair audio do video, no momento dertemindo
from gtts import gTTS # gravando de audio, atraves da srt
from time import sleep # Tempo em segundos 
from os import system # excuta comando no sistema
from tools.SubTitle import code_read, print_srt # extrair informação da legenda
from tools.minical import seg_calminis # tempos do video

system("clear")
write_bannes()
sleep(2.0)
os.system("clear")
blue_bannes()
# Cores do terminal
red    = '\033[1;31m'
blue   = '\033[1;34m'
gray   = '\033[1;37m'
green  = '\033[0;32m'
write  =  '\033[0;37m'
yellow = '\033[1;33m'
yellow_ = '\033[5;33m'
# valores diferentes 
n      = 0 
num    = 1
gord   = 0
daemon = 0 

# criando listas
list_1      = []
list_2      = []
list_3      = []
list_4      = []
list_5      = []
time_srt    = []
dict_valor  = []
dict_chave  = []

# dicionario
time_dist = {}

print(f"\n{gray}[ {red}!{gray} ] {yellow_}ATENÇÃO{write}{gray}: Esse script está em fazer de desenvolvimento,\nEntrão não espere muito dele.")
# Escolha do usuário
print(f"\n[ {blue}*{gray} ] Escolha o video", end='')

video_ = input(f" {yellow}>>{write} ")

print(f"{gray}[ {blue}*{gray} ] Escolha o arquivo SRT do video", end='')
legenda = input(f" {yellow}>>{write} ")

srt_time = code_read(legenda)
Sub_time     = srt_time[0]
Sub_srt      = srt_time[1]
Sub_sequence = srt_time[2]

print_srt(srt_time)
sleep(0.5)


# Transformando tudo que seja hora ou minuntos para segundos
def convert_seg(time):
    split_  = time.split(":")
    
    hora = float(split_[0])
    mins = float(split_[1])
    segs = float(str(split_[2]).replace(',', '.'))
    
    homin = hora*60 # Transformando hora em minuntos
    vmin = homin*60 # transformando minutos em segundos
    fixed = (mins*60) + segs + vmin

    return fixed

# subitaindo tempo incial e final
def time_if(time1, time2):
    subs1 = convert_seg(time1)
    subs2 = convert_seg(time2)
    total = subs1 - subs2

    return round(abs(total),1)

# Controlando á acelelação do robo
def Controlar_voz_time(slep1, slep2, sry, audio_):
    
    info = mediainfo(sry)
    duration_ = str(info["duration"])

    Sd = str(duration_.split('.')[0]) + str('.') + str(duration_.split('.')[1][0:1])
    voz_robot = str()
    for i in range(1,101):
        fidex = 1.0   
        so = round(float(Sd) - i / 10, 1)
        tyis = round(fidex+round(i*10/1000,3),3)
        funtime = time_if(slep1, slep1)
        
        if str(so) == str(funtime):
            voz_robot = str(tyis)
            break

    system(f'ffmpeg -i {sry} -filter:a "atempo={voz_robot}" -vn {audio_} 2>/dev/null')

# ira corta a parte do enfeito sonoro onde o personagem não fala

def Cort_audio(timpe_i, time_f, vaudio): 
    video = VideoFileClip(video_)

    start_i = timpe_i
    ivstart = convert_seg(start_i)
    start_f = time_f
    fvstart = convert_seg(start_f)

    start_cort = video.subclip(ivstart+00.215, fvstart-00.215)
    stringv = "audio/audio_" + str(vaudio) + ".mp3"
    start_cort.audio.write_audiofile(stringv)

# Fantimento do tempo da legenda, onde o robo poder ou não fala
def Fantimento_Time(t1, t2, dist_):
    fant_time = []
    F_time1 = t1[len(t1)-12:].replace(',', '.')
    F_time2 = t2[0:12].replace(',', '.')

    fant_time.append([F_time1, F_time2])
    time_dist.update({dist_:fant_time})

# Buscando intervalo no qual momento o robo vai para de fala
# é o que o programa vai fazer adianter

def Cal_time(t):

    x = 0
    n_ = len(t)
    cal_num = 0
    
    while True:
        cal_num += 1
        if x >= n_-1:
            break
        else:
            pass
        valor_1 = t[x]
        v = valor_1[len(valor_1)-6:].replace(',', '.')
        try:
            valor_2 = t[x+1]
        except: 
            pass
        v_ = valor_2[6:-17].replace(',', '.')

        cal = float(v) - float(v_)
        cal_final = round(abs(cal))
        
        if int(cal_final) == int(1) or int(cal_final) != int(0):
            Fantimento_Time(valor_1, valor_2, cal_num)
        x += 1

Cal_time(Sub_time)

chave = time_dist.keys()
valor = time_dist.values()

for dict1 in chave:
    dict_chave.append(dict1)

for dict2 in valor:
    dict_valor.append(dict2)


def Grava(voz_grava, numo):
    
    # Gravando audio
    mode = gTTS(text=voz_grava, lang='pt-br', slow=False)

    # Salvando audio em um arquivo MP3
    sry = 'audio/voz_robo.mp3'
    audio_ = 'audio/audio_' + str(numo) + '.mp3'
    mode.save(sry)

    print("[ + ] Gravando audio ", numo)
    
    return sry, audio_

print(f"\n[ {yellow}+{gray} ] Inciando Fantiamento de gravação.")    


if str(Sub_time[0][0:12]) == '00:00:00,000':
    time_audio = Grava(Sub_srt[0], 1)
    # Aqual valor corta
    time_srt1 = Sub_time[0][0:12]
    time_srt2 = Sub_time[0][len(Sub_time[0])-12:]
    Controlar_voz_time(time_srt1, time_srt2, time_audio[0], time_audio[1])
else:
    Cort_audio("00:00:00.000", Sub_time[0][0:12], 1)

incial = 2
numomas = len(Sub_sequence) + len(dict_valor)

for total in range(0,numomas):

    try:
        if total not in dict_chave:
            time_audio = Grava(Sub_srt[total], incial)
            time_srt1 = Sub_time[total][0:12] 
            time_srt2 = Sub_time[total][len(Sub_time[total])-12:]
            Controlar_voz_time(time_srt1, time_srt2, time_audio[0], time_audio[1])
            incial += 1
        else:
            # Time in chave and values
            time_inicial = dict_valor[0][0][0]
            time_final = dict_valor[0][0][1]               
            audio_time = Grava(Sub_srt[total], incial)
                        
            Cort_audio(time_inicial, time_final, incial+1)

            # Aqual valor corta
            time_srt1 = Sub_time[total][0:12]
            time_srt2 = Sub_time[total][len(Sub_time[total])-12:]

            Controlar_voz_time(time_srt1, time_srt2, audio_time[0], audio_time[1])                 
            dict_valor.pop(0)
            incial += 2
    except Exception as er:
        print("ERROR: ", er)
        break

file_ = open('audio/mylist.txt', 'w')

i = incial
ts_ = Sub_time[len(Sub_time)-1][len(Sub_time[len(Sub_time)-1])-12:]
mini_seg = seg_calminis(video_)  

if ts_[0:8] == mini_seg:
    pass
else:
    Cort_audio(ts_, mini_seg, i)


for numsd in range(1,incial+1):
    fidf = "file 'audio_" + str(numsd) + ".mp3'" + "\n"
    file_.writelines(fidf)

file_.close()

def String_name(string_video):
    stg = 1
    video_name = ''.join(list(reversed(string_video)))
    for sv in video_name:
        if str(sv) == '/':
            break
        else:
            stg += 1
    vg = string_video[len(string_video)-stg+1:]
    return vg

print(f"{gray}[ {yellow}+{gray} ] Quase chegando ao fim !")
# Acortando title da string do video Original
# Fazendo tunelamento com audio gravando com ffmpeg

# mesclar muitos arquivos mp3
system("ffmpeg -f concat -safe 0 -i audio/mylist.txt -c copy output.mp3 2>/dev/null")
sleep(0.5)

# Remove audio
system(f"ffmpeg -i {video_} -c copy -an saida_video.mp4 2>/dev/null")
sleep(0.5)

# Adicionado audio ao video
system("ffmpeg -i saida_video.mp4 -i output.mp3 -codec copy -shortest input.mp4 2>/dev/null")
sleep(0.5)

# Adicionar legenda no video
system(f"ffmpeg -i input.mp4 -i {legenda} -map 0 -map 1 -c copy -c:s mov_text {String_name(video_)[0:len(String_name(video_))-4]}_Modificado.mp4 2>/dev/null")
sleep(0.5)

# Clear
system("rm input.mp4 saida_video.mp4 output.mp3 audio/*.mp3 audio/mylist.txt")
sleep(0.5)

print(f"{gray}[ {blue}*{gray} ] Arquivo de log salvo na pasta Log ...")

date_now = datetime.now().strftime('%d/%m/%y')
hour_now = datetime.now().astimezone(timezone(timedelta(hours=-3))).strftime('%H:%M:%S')
file_log = "Log/" + str(String_name(video_)[0:len(String_name(video_))-4]) + "_" + str(date_now).replace('/', '.') + "_|_" + str(hour_now) + ".txt"
log = open(file_log, "w")
log.writelines("    Video Modificado   \n")
log.writelines("Dia:                        " + str(date_now) + "\n")
log.writelines("Hora:                       "+ str(hour_now) + "\n")
log.writelines("Nome: do Video:             "+ str(String_name(video_)) + "\n")
log.writelines("Nome da Legenda do Video:   "+ str(String_name(legenda)) + "\n")

print(f"{gray}[ {yellow}+{gray} ] Video salvo: {blue}", str(String_name(video_)[0:len(String_name(video_))-4])+"_Modificado.mp4")
print(f"\n{gray}[ {blue}*{gray} ] Pronto !!!")
