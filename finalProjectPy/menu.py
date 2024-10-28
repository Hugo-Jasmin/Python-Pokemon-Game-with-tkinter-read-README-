import random
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
Menu = tk.Tk()
Menu.geometry("600x400")
Menu.title("Main Menu")

background = tk.Frame(Menu)
background.pack()
def rosdonfsoa():
    os.system('pokebackup.py')

# Load and set the background image
background = tk.Canvas(Menu, width=600, height=400)
background.pack(fill="both", expand=True)

bg_image = ImageTk.PhotoImage(Image.open("menu/background1.png").resize((600,400)))
background.create_image(0, 0, image=bg_image, anchor="nw")

# Add widgets on top of the background (for example, a button)
playGame = tk.Button(Menu, text="Play Game", command=rosdonfsoa)
background.create_window(300, 150, window=playGame, width=400)

# Leaderboard Button
leaderboard = tk.Button(Menu, text="Check LeaderBoard", command=lambda: print("Checking Leaderboard"))
background.create_window(300, 200, window=leaderboard, width=400)

# Unlocks Button
unlocks = tk.Button(Menu, text="Check Unlocks", command=lambda: print("Checking Unlocks"))
background.create_window(300, 250, window=unlocks, width=400)


Menu.mainloop()