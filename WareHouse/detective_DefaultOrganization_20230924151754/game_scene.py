'''
This file contains the GameScene class, which represents the main game scene.
'''
from tkinter import Tk, Label, Button
class GameScene:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sherlock Holmes: Murder Investigation")
        self.window.geometry("800x600")
        self.title_label = Label(self.window, text="Sherlock Holmes: Murder Investigation", font=("Arial", 24))
        self.title_label.pack(pady=20)
        self.start_button = Button(self.window, text="Start Investigation", font=("Arial", 16), command=self.start_investigation)
        self.start_button.pack(pady=10)
    def start(self):
        self.window.mainloop()
    def start_investigation(self):
        # TODO: Implement the investigation scene
        pass