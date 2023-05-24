import tkinter as tk

def drag(event):
    #to make it possible to drag all widgets and not just label, we type the ff
    widget = event.widget
    #then we change all 'label' to 'widget'
    #get the co-ordinate where we clicked wihtin the label then assign it to a new variable of our label
    #label.startX=event.x #give x co-ordinates within the clicked domain of the label
    widget.startX=event.x
    #label.startY=event.y #give y co-ordinates within the clicked domain of the label
    widget.startY=event.y

def drag_m(event):
    widget = event.widget
    #we create new x and y co-ordinates
    x = widget.winfo_x() - widget.startX + event.x #gets top left x co-ordinates of label relative to the current positon 
    y = widget.winfo_y() - widget.startY + event.y #top left corner, place clicked, place we between dragging widget to
    widget.place(x=x,y=y)


root = tk.Tk()
#how to drag and dropt widgets in python
label = tk.Label(root, bg='red', width=10, height=5)
label.place(x=0, y=0)
label.bind('<Button-1>', drag) #left mouse button
label.bind('<B1-Motion>', drag_m) #left mouse button held and being dragged

l = tk.Label(root, bg='green', width=10, height=5)
l.place(x=50, y=100)
l.bind('<Button-1>', drag) #left mouse button
l.bind('<B1-Motion>', drag_m) #left mouse button held and being dragged



root.mainloop()