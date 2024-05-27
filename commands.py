import os as os
from tkinter import filedialog
import tkinter as tk

songs = []
paused = False
current_song = ""

def load_music(root):
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext  = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

