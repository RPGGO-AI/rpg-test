from tkinter import Tk, Canvas
from dragon import Dragon
root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()
dragon = Dragon(canvas)
dragon.draw()
root.mainloop()