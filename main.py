import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("500x600")

pygame.mixer.init()

songlist = tk.Listbox(root, bg = "black", fg = "white", width = 100, height = 15)
songlist.pack()

imageAssets = ["backward_button.png", "play_button.png", "pause_button.png", "forward_button.png"]
images = {}

controlFrame = tk.Frame(root)
controlFrame.pack()

for imageFile in imageAssets:
    # print(f"Assets/{imageFile}")
    pilImage = Image.open(f"Assets/{imageFile}")
    images[imageFile] = ImageTk.PhotoImage(pilImage)

controlButtons = []
for i, imageFile in enumerate(imageAssets):
    button = tk.Button(controlFrame, image = images[imageFile], borderwidth=0)
    button.grid(row = 0, column = i)
    controlButtons.append(button)

# playButtonLabel = tk.Label(root, image = playButtonImage)
# playButtonLabel.pack()


root.mainloop()

