import pygame
from pytube import YouTube

# Initialize Pygame
pygame.init()

# Set up the music player
pygame.mixer.init()

# Set the YouTube link
youtube_link = "https://youtu.be/jADTdg-o8i0?si=vXdpIFCd9PffQmQd"

# Download the YouTube video as an audio file
yt = YouTube(youtube_link)
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()

# Get the downloaded file name
downloaded_file = audio_stream.title + ".webm"

# Load the downloaded song
pygame.mixer.music.load(downloaded_file)

# Function to play the current song
def play_music():
    pygame.mixer.music.play()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Main loop
while True:
    user_input = input("Enter command (play/stop/exit): ").lower()

    if user_input == 'play':
        play_music()
    elif user_input == 'stop':
        stop_music()
    elif user_input == 'exit':
        pygame.quit()
        quit()
    else:
        print("Invalid command. Try again.")