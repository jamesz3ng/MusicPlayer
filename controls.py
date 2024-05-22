import tkinter as tk
from PIL import Image, ImageTk


def process_image(imageAssets : list, images : dict):

    for imageFile in imageAssets:
        pilImage = Image.open(f"Assets/{imageFile}")
        images[imageFile] = ImageTk.PhotoImage(pilImage)


def make_controls(imageAssets : list, images: dict, controlFrame):
    for i, imageFile in enumerate(imageAssets):
        button = tk.Button(controlFrame, image = images[imageFile], borderwidth=0)
        button.grid(row = 0, column = i)
        # controlButtons.append(button)
