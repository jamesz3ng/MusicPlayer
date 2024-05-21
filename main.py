from tkinter import *
from PIL import Image, ImageTk
import pygame
import os


root = Tk()
root.title("Music Player")
root.geometry("500x600")

pygame.mixer.init()

songlist = Listbox(root, bg = "black", fg = "white", width = 100, height = 15)
songlist.pack()


imageAssets = ["backward_button.png", "forward_button.png", "pause_button.png", "play_button.png"]
images = {}

for imageFile in imageAssets:
    # print(f"Assets/{imageFile}")
    pilImage = Image.open(f"Assets/{imageFile}")

controlButtons = []
# for imageFile in imageAssets:
#     button = tk.



pilPlayButton = Image.open("Assets/play_button.png")
playButtonImage = ImageTk.PhotoImage(pilPlayButton)







playButtonLabel = Label(root, image = playButtonImage)
playButtonLabel.pack()



root.mainloop()

