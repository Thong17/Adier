import os
from moviepy.editor import *
from app import app
from pytube import YouTube
from flask import render_template, redirect, request, jsonify

@app.route('/')
def index():
    return render_template('views/index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['input']
    ytb = YouTube(url).streams.first().download(r'audio')

    mp3 = ytb.split('.')[0]+'.mp3'

    videoclip = VideoFileClip(ytb)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3)
    audioclip.close()
    videoclip.close()

    os.remove(ytb)

    return jsonify('Success')