import os
from moviepy.editor import *
from app import app
from pytubefix import YouTube
from pytubefix.cli import on_progress
from flask import render_template, redirect, request, jsonify
import yt_dlp

def download_youtube_video(url, output_dir='.'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set up yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Output file template
    }

    # Download the video and retrieve the video title
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)  # Extract info and download
        video_title = info_dict['title']  # Get the video title

    return video_title  # Return the video name

@app.route('/')
def index():
    return render_template('views/index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['input'].split('&list')[0]
    ytb = download_youtube_video(url)

    print('=============================')
    print(ytb)
    print('=============================')

    mp3 = ytb.split('.')[0]+'.mp3'

    videoclip = VideoFileClip(ytb + '.mp4')
    audioclip = videoclip.audio
    audioclip.write_audiofile('./audio/' + mp3)
    audioclip.close()
    videoclip.close()

    os.remove(ytb + '.mp4')

    return jsonify('Success')

def convert_youtube_video(url, output_dir='./audio/'):
    mp3 = url.split('.')[0]+'.mp3'

    videoclip = VideoFileClip(url + '.mp4')
    audioclip = videoclip.audio
    audioclip.write_audiofile(output_dir + mp3)
    audioclip.close()
    videoclip.close()

    os.remove(url + '.mp4')

@app.route('/convert')
def convert():
    url = 'Sezairi - It’s You (Lyrics) - You, youre my love, my life, my beginning'
    convert_youtube_video(url)
    return jsonify('Success')


    

