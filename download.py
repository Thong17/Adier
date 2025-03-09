from pytube import YouTube

def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    # download the video
    video.download(path)

# example usage:
download_video_from_youtube('https://www.youtube.com/watch?v=c1l7IySwH80', './video')