'''
This file contains the Dragon class that represents the dragon to be drawn.
'''
class Dragon:
    def __init__(self, canvas):
        self.canvas = canvas
    def draw(self):
        # Implement the logic to draw the dragon on the canvas
        # You can use canvas.create_line, canvas.create_polygon, etc.
        # to draw the different parts of the dragon
        self.canvas.create_polygon(100, 100, 200, 200, 300, 100, fill="green")
        self.canvas.create_polygon(200, 200, 300, 300, 400, 200, fill="green")
        self.canvas.create_polygon(300, 100, 400, 200, 500, 100, fill="green")
        self.canvas.create_polygon(400, 200, 500, 300, 600, 200, fill="green")
        self.canvas.create_polygon(500, 100, 600, 200, 700, 100, fill="green")