from importlib.resources import path
from flask import Flask, render_template, request, send_file
import os
import re

import moviepy.editor as mp
from pytube import YouTube

app = Flask(__name__)
path = "C:/Users/franc/Music/Musicas" + "/"

@app.route('/')
def route():
    return render_template("index.html")

@app.route('/envia', methods=['GET','POST'])
def envia():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        ys = yt.streams.filter(only_audio=True).first().download(path)

        for file in os.listdir(path):
            if re.search('mp4',file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

        print ("Sucesso! ")
    return render_template("sucesso.html")#send_file(p, as_attachment=True)

if __name__ == '__main__':
    app.run(host ='localhost')