import tkinter as tk
import os

def make_menu(root):
    menubar = tk.Menu(root)
    root.config(menu = menubar)

    organise_menu = tk.Menu(menubar)
    menubar.add_cascade(label="Organise", menu=organise_menu)
    organise_menu.add_command(label = "Select Folder")


