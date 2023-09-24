'''
This file contains the GameScene class, which represents the main gameplay scene of the Sherlock Holmes RPG game.
'''
import tkinter as tk
from tkinter import messagebox
from investigation_scene import InvestigationScene
class GameScene:
    def __init__(self, window):
        self.window = window
    def start_game(self):
        # Display the game introduction
        messagebox.showinfo("Welcome", "Welcome to the Sherlock Holmes RPG game! Your mission is to investigate a murder case.")
        # Create a button to start the investigation
        start_button = tk.Button(self.window, text="Start Investigation", command=self.start_investigation)
        start_button.pack()
    def start_investigation(self):
        # Hide the start button
        start_button = self.window.pack_slaves()[0]
        start_button.pack_forget()
        # Create an investigation scene object
        investigation_scene = InvestigationScene(self.window)
        # Start the investigation
        investigation_scene.start_investigation()