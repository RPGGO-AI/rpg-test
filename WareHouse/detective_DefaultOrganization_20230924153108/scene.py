'''
This file defines the Scene class, which represents the scenes in the "Sherlock Holmes: Murder Investigation" game.
'''
class Scene:
    def __init__(self, name, description, background_story, goal, characters):
        self.name = name
        self.description = description
        self.background_story = background_story
        self.goal = goal
        self.characters = characters
    def enter(self):
        # TODO: Implement scene entry logic
        pass
    def exit(self):
        # TODO: Implement scene exit logic
        pass
    def interact(self):
        # TODO: Implement scene interaction logic
        pass