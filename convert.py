from moviepy.editor import *

# Load the video file
audio = AudioFileClip("DJ Mama Afrika bbhc mengkane [DAPP FX].mp4")

# Extract the audio from the video

# Save the audio to an MP3 file
audio.write_audiofile("output_audio.mp3", codec='libmp3lame')

# Close the video file
audio.close()