import tkinter as tk

def move_up(event):
    canvas.move(myimg, #the image loaded
                0, #keep x the same
                -10) #reduce 10 from where y is

def move_down(event):
    canvas.move(myimg, #the image loaded
                0, #keep x the same
                +10) #increases 10 from where y is

def move_left(event):
    canvas.move(myimg, #the image loaded
                -10, #reduces x making it move left
                0) #keeps y 

def move_right(event):
    canvas.move(myimg, #the image loaded
                +10, #increases x causing it to move right
                0) #keeps 10 
root = tk.Tk()
root.geometry('600x600')

#moving an object in a canvas
root.bind('<w>', move_up)
root.bind('<a>', move_left)
root.bind('<s>', move_down)
root.bind('<d>', move_right)
root.bind('<Up>', move_up)
root.bind('<Left>', move_left)
root.bind('<Down>', move_down)
root.bind('<Right>', move_right)

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.config(bg='grey')

img = tk.PhotoImage(file='spaceShip.png')
myimg = canvas.create_image(0, 0, image=img, anchor='nw') #NW --north west



root.mainloop()