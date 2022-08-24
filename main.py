from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg
import moviepy.editor as mp
import re
import os

link = input ("Link do video: ")
path = input ("Pasta onde o video sera salvo: ")
yt = YouTube(link)

print ("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Pronto!")

print("Convertendo para MP3...")
for file in os.listdir(path):
    if re.search('mp4',file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print ("Sucesso!")