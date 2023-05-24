import tkinter as tk

def move_up(event):
    label.place(x=label.winfo_x(), # the length of x remains unchanged
                y=label.winfo_y()-10 # the length of y reduces by 10 causing it to move up
                )
    
def move_left(event):
    label.place(x=label.winfo_x()-10, # the length of x reduces by 10 causing it to move left
                y=label.winfo_y() # the length of y remains unchanged
                )
    
def move_down(event):
    label.place(x=label.winfo_x(), # the length of x remains unchanged
                y=label.winfo_y()+10 # the length of y increases by 10 causing it to move down
                )
    
def move_right(event):
    label.place(x=label.winfo_x()+10, # the length of x increses by 10 
                y=label.winfo_y() # the length of y remains unchanged 
                )

root = tk.Tk()
root.geometry('500x500')

#moving an object in the window
root.bind('<w>', move_up)
root.bind('<a>', move_left)
root.bind('<s>', move_down)
root.bind('<d>', move_right)
root.bind('<Up>', move_up)
root.bind('<Left>', move_left)
root.bind('<Down>', move_down)
root.bind('<Right>', move_right)
img = tk.PhotoImage(file='spaceShip.png')
label=tk.Label(root,
               image=img,
               )
label.place(x=0,y=250)



root.mainloop()