'''
This file contains the InvestigationScene class, which represents the scene where the player investigates the murder case.
'''
import tkinter as tk
from tkinter import messagebox
from suspect import Suspect
class InvestigationScene:
    def __init__(self, window):
        self.window = window
        self.suspects = [
            Suspect("John Smith", "Businessman"),
            Suspect("Emily Johnson", "Actress"),
            Suspect("Thomas Davis", "Doctor")
        ]
    def start_investigation(self):
        # Display the investigation scene
        messagebox.showinfo("Investigation", "You are now in the investigation scene. Choose a suspect to interrogate.")
        # Create buttons for each suspect
        for suspect in self.suspects:
            button = tk.Button(self.window, text=suspect.name, command=lambda s=suspect: self.interrogate_suspect(s))
            button.pack()
    def interrogate_suspect(self, suspect):
        # Hide the suspect buttons
        for button in self.window.pack_slaves():
            button.pack_forget()
        # Display the suspect's information
        messagebox.showinfo("Suspect Information", f"Name: {suspect.name}\nOccupation: {suspect.occupation}")
        # Continue the investigation
        messagebox.showinfo("Investigation", "Continue investigating...")