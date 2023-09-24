'''
This is the main file of the Sherlock Holmes RPG game. It imports the necessary modules and starts the game.
'''
import tkinter as tk
from tkinter import messagebox
from game_scene import GameScene
# Create the main game window
window = tk.Tk()
window.title("Sherlock Holmes RPG Game")
# Create a game scene object
game_scene = GameScene(window)
# Start the game
game_scene.start_game()
# Run the main event loop
window.mainloop()