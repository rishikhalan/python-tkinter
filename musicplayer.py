
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory 
import os


#initialize pygame
pygame.init()
pygame.mixer.init()

# Initialize Tkimter window
music_player = Tk()
music_player. title("My Music Player")
music_player.geometry("450x350")

#Ask the user to select a directory and change the working directory
directory = askdirectory()
os.chdir(directory)
song_list = os. listdir()


def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()


#create a label to display the currently playing song
var = StringVar()
song_title = Label(music_player , font = "Helvetica 15 bold" , textvariable=var , bg = "#fff" , fg = "#000000")
song_title.pack(pady = 10)



# Create buttons with improved color schemes
Button1 = Button(music_player, width=8, height=2, font="Helvetica 12 bold", text="PLAY", command=play, bg="#4CAF50", fg="white")
Button1.pack(fill="x", padx=10, pady=5)
Button2 = Button(music_player, width=8, height=2, font="Helvetica 12 bold", text="STOP", command=stop, bg="#F44336", fg="white")
Button2.pack(fill="x", padx=10, pady=5)
Button3 = Button(music_player, width=8, height=2, font="Helvetica 12 bold", text="PAUSE", command=pause, bg = "#FFC107", fg="black")
Button3.pack(fill="x", padx=10, pady=5)
Button4 = Button(music_player, width=8, height=2, font="Helvetica 12 bold", text="RESUME", command=resume, bg="#03A9F4", fg="white")
Button4.pack(fill="x", padx=10, pady=5)



# Create a Listbox to display the list of songs
play_list = Listbox(music_player, font="Helvetica 17 bold", bg='#f5f5f5', selectmode=SINGLE)

# Insert the songs into the Listbox
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
play_list.pack(fill="both", expand=True, padx=10, pady=10)

# Start the Tkinter event loop
mainloop()