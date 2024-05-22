import tkinter as tk
from PIL import Image, ImageTk
from controls import process_image, make_controls
import pygame
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("380x350")

pygame.mixer.init()

songlist = tk.Listbox(root, bg = "black", fg = "white", width = 100, height = 15)
songlist.pack()

imageAssets = ["backward_button.png", "play_button.png", "pause_button.png", "forward_button.png"]
images = {}
controlButtons = []

controlFrame = tk.Frame(root)
controlFrame.pack()

process_image(imageAssets, images)

make_controls(imageAssets, images, controlFrame)




root.mainloop()

