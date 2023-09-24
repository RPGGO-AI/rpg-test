'''
This file contains the GameScene class, which represents the main game scene.
'''
class GameScene:
    def __init__(self, window):
        self.window = window
        self.current_scene = None
        # Load the initial scene
        self.load_scene("crime_scene")
    def load_scene(self, scene_name):
        # Destroy the current scene if it exists
        if self.current_scene:
            self.current_scene.destroy()
        # Load the new scene
        if scene_name == "crime_scene":
            self.current_scene = CrimeScene(self.window, self)
        elif scene_name == "interrogation_scene":
            self.current_scene = InterrogationScene(self.window, self)
        elif scene_name == "evidence_scene":
            self.current_scene = EvidenceScene(self.window, self)
        else:
            messagebox.showerror("Error", "Invalid scene name!")
        # Pack the current scene
        self.current_scene.pack()
    def go_to_next_scene(self):
        # Determine the next scene based on the current scene
        if isinstance(self.current_scene, CrimeScene):
            next_scene = "interrogation_scene"
        elif isinstance(self.current_scene, InterrogationScene):
            next_scene = "evidence_scene"
        else:
            next_scene = "crime_scene"
        # Load the next scene
        self.load_scene(next_scene)
class CrimeScene(tk.Frame):
    def __init__(self, parent, game_scene):
        super().__init__(parent)
        self.game_scene = game_scene
        # Crime scene description
        self.description_label = tk.Label(self, text="You arrive at the crime scene. The victim, Mr. John Doe, lies dead on the floor.")
        self.description_label.pack()
        # Investigate button
        self.investigate_button = tk.Button(self, text="Investigate", command=self.investigate)
        self.investigate_button.pack()
    def investigate(self):
        # Display investigation results
        messagebox.showinfo("Investigation", "You find a torn piece of paper with a partial address.")
        # Go to the next scene
        self.game_scene.go_to_next_scene()
class InterrogationScene(tk.Frame):
    def __init__(self, parent, game_scene):
        super().__init__(parent)
        self.game_scene = game_scene
        # Suspect interrogation
        self.description_label = tk.Label(self, text="You bring in the main suspect for interrogation.")
        self.description_label.pack()
        # Question button
        self.question_button = tk.Button(self, text="Ask Question", command=self.ask_question)
        self.question_button.pack()
    def ask_question(self):
        # Display suspect's response
        messagebox.showinfo("Interrogation", "The suspect denies any involvement in the murder.")
        # Go to the next scene
        self.game_scene.go_to_next_scene()
class EvidenceScene(tk.Frame):
    def __init__(self, parent, game_scene):
        super().__init__(parent)
        self.game_scene = game_scene
        # Evidence examination
        self.description_label = tk.Label(self, text="You examine the torn piece of paper found at the crime scene.")
        self.description_label.pack()
        # Examine button
        self.examine_button = tk.Button(self, text="Examine", command=self.examine)
        self.examine_button.pack()
    def examine(self):
        # Display examination results
        messagebox.showinfo("Examination", "The torn piece of paper contains an address that leads to a suspicious warehouse.")
        # Go to the next scene
        self.game_scene.go_to_next_scene()