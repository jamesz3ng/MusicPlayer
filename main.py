import tkinter as tk
from PIL import Image, ImageTk
from controls import process_image, make_controls, images, imageAssets
import pygame

# Initialize the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("380x350")

# Initialize the Pygame mixer
pygame.mixer.init()

# Create the song list
songlist = tk.Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

# Define the control frame
controlFrame = tk.Frame(root)
controlFrame.pack(side=tk.BOTTOM, fill=tk.X)

# Process images and create controls
process_image(imageAssets, images)
make_controls(imageAssets, images, controlFrame)

# Start the Tkinter main loop
root.mainloop()
