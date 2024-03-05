import pygame
from tkinter import Tk, Button

# Replace "song.mp3" with the actual path to your music file
song_path = "game_state_music.mp3"

# Flag to track pause state
is_paused = False

def play_music():
    global is_paused
    if pygame.mixer.init():
        pygame.mixer.music.load(song_path)
        if not is_paused:
            pygame.mixer.music.play()

def pause_music():
    global is_paused
    if pygame.mixer.get_init():
        if is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        is_paused = not is_paused

# Initialize Tkinter and Pygame
root = Tk()
root.title("Music Player")
root.geometry('500x500')

play_button = Button(root, text="Play/Pause", command=pause_music)
play_button.pack()
pygame.mixer.init()
play_music()

# Main loop to keep the window open
root.mainloop()

# Quit Pygame when the window closes
pygame.quit()
