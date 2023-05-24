import tkinter as tk
import time
#we import a python file here
from ball import *

#a constant is a variable which remians unchanged
WIDTH = 500
HEIGHT = 500
#we create two velocities or speed to measure how fast the image is changing with coordinates

root = tk.Tk()
root.geometry('500x500')

#animating an image in tkinter

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
#canvas.config(bg='grey')

#creating multiple circles
volleyball=ball(canvas, 0, 0, 100, 1, 1, 'white') #entering the parameters constructed in ball class
tennisball=ball(canvas, 0, 0, 50, 4, 3, 'yellow')
pinball=ball(canvas, 0, 0, 30, 3, 6, 'pink')

# while running, let's move our ball
while(True):
    volleyball.move()
    tennisball.move()
    pinball.move()
    #update the window so that it refreshes
    root.update()
    #delay time
    time.sleep(0.01)

root.mainloop()