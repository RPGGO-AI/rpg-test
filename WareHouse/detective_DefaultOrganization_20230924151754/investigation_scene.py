'''
This file contains the InvestigationScene class, which represents the scene where the player investigates the murder case.
'''
from tkinter import Label, Button
class InvestigationScene:
    def __init__(self, game_scene):
        self.game_scene = game_scene
        self.game_scene.title_label.config(text="Investigation Scene")
        self.game_scene.start_button.config(text="Continue", command=self.continue_investigation)
        self.investigation_label = Label(self.game_scene.window, text="You are Sherlock Holmes, the famous detective. A murder has occurred in London and you have been called to investigate.", font=("Arial", 16))
        self.investigation_label.pack(pady=20)
        self.clue_button = Button(self.game_scene.window, text="Examine Clues", font=("Arial", 16), command=self.examine_clues)
        self.clue_button.pack(pady=10)
    def continue_investigation(self):
        # TODO: Implement the continuation of the investigation scene
        pass
    def examine_clues(self):
        # TODO: Implement the clue examination scene
        pass