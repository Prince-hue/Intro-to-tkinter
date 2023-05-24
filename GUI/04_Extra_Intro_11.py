import tkinter as tk
import time

#a constant is a variable which remians unchanged
WIDTH = 500
HEIGHT = 500
#we create two velocities or speed to measure how fast the image is changing with coordinates
xVelocity = 10
yVelocity = 10
root = tk.Tk()
root.geometry('600x600')

#animating an image in tkinter

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.config(bg='grey')
#to add a background image
#bimg = tk.PhotoImage(file='spaceShip.png')
#bmyimg = canvas.create_image(0, 0, image=img, anchor='nw')
img = tk.PhotoImage(file='spaceShip.png')
myimg = canvas.create_image(0, #x position
                             0, #y position
                             image=img, anchor='nw') #NW --north west --top left corner
#assigning two variables to the img width and height
img_w = img.width()
img_h = img.height()

while (True):
    #we want to co-ordinates from the canvas but this would return a list so we create a list
    coordinates = canvas.coords(myimg)
    #lets print to see the coordinates of the img on the canvas
    print(coordinates)
    # we want the img to bounce off when it hits the borders
    if (coordinates[0]>=(WIDTH-img_w) or coordinates[0]<0):
        xVelocity=-xVelocity
    if (coordinates[1]>=(HEIGHT-img_h) or coordinates[1]<0):
        yVelocity=-yVelocity
    #update the position of the image for each iteration
    canvas.move(myimg, xVelocity, yVelocity) #takes three arguments ie the img u want to move, how far on x, how far on y
    root.update() #we update the window on any changes
    time.sleep(0.01) #he programs delays for 1 hundredth of a sec



root.mainloop()