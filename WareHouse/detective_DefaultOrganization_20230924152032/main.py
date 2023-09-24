'''
This is the main file of the RPG game "Sherlock Holmes: Murder Investigation".
The game is set in Victorian London, where you play as Sherlock Holmes, the famous detective. Your goal is to investigate a murder case and uncover the truth behind it.
'''
# Import necessary modules
import tkinter as tk
from tkinter import messagebox
from game_scene import GameScene
# Create the main game window
window = tk.Tk()
window.title("Sherlock Holmes: Murder Investigation")
window.geometry("800x600")
# Create a game scene object
game_scene = GameScene(window)
# Start the game loop
window.mainloop()