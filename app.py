from importlib.resources import path
from flask import Flask, render_template, request, Response,redirect, send_file
import os
from os import remove
import pafy
import moviepy.editor as mp

app = Flask(__name__)
path = os.getcwd() + "/"

@app.route('/')
def route():
    return render_template("index.html")

@app.route('/envia', methods=['GET','POST'])
def envia():
    if request.method == 'POST':
        url = request.form['url']
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        best.download(path)
        name = path + video.title + ".mp4"
        clip = mp.VideoFileClip(name)
        clip.audio.write_audiofile(path + video.title + ".mp3")
        p = path + video.title + ".mp3"
        print (video.title)
        return send_file(p, as_attachment=True)

if __name__ == '__main__':
    app.run(host ='localhost')