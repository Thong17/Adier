import os
from moviepy.editor import *
from app import app
from pytubefix import YouTube
from pytubefix.cli import on_progress
from flask import render_template, redirect, request, jsonify
from pydub import AudioSegment


@app.route('/')
def index():
    return render_template('views/index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['input'].split('&list')[0]
    
    yt = YouTube(url, on_progress_callback = on_progress)
    ytb = yt.streams.get_audio_only()
    ytb.download()
    return jsonify('Success')