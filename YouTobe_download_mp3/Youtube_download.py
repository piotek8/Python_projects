import pytube
from moviepy.editor import *

while True:
    # Prompt user to enter YouTube video link
    link = input("Enter YouTube video link or write 'exit' to quit: ")
    
    # If you write 'exit' the program turn off
    if link.lower() == 'exit': #
        break
    
    # Create a YouTube object using the link
    youtube = pytube.YouTube(link)
    
    # Get the audio stream of the YouTube video
    audio_stream = youtube.streams.filter(only_audio=True).first()
    
    # Download the audio stream to an MP3 file in the specified directory
    audio_stream.download(output_path='C:\\Users\\Piotr\\Downloads\\', filename=youtube.title + '.mp3')
    
    # Load the downloaded audio file using AudioFileClip
    audio_file = AudioFileClip('C:\\Users\\Piotr\\Downloads\\' + youtube.title + '.mp3')
    
    # Save the audio file as an MP3 file in the specified directory
    audio_file.write_audiofile('C:\\Users\\Piotr\\Downloads\\' + youtube.title + '.mp3')
    
    print("MP3 audio file has been downloaded and saved as", 'C:\\Users\\Piotr\\Downloads\\' + youtube.title + ".mp3")
