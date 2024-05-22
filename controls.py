from PIL import Image, ImageTk
import tkinter as tk
import os

# Define imageAssets in controls.py
imageAssets = ["backward_button.png", "play_button.png", "pause_button.png", "forward_button.png"]

# Initialize images dictionary in controls.py
images = {}

def process_image(imageAssets, images):
    for imageFile in imageAssets:
        try:
            pilImage = Image.open(os.path.join("Assets", imageFile))
            images[imageFile] = ImageTk.PhotoImage(pilImage)
            print(f"Loaded image: {imageFile}")
        except Exception as e:
            print(f"Error loading image {imageFile}: {e}")

def make_controls(imageAssets, images, controlFrame):
    controlButtons = []
    for i, imageFile in enumerate(imageAssets):
        button = tk.Button(controlFrame, image=images[imageFile], borderwidth=0)
        button.grid(row=0, column=i)
        controlButtons.append(button)
