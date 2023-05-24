import tkinter as tk
root = tk.Tk()

#functions
def mykey(event):
    #print('you pressed a key', event.keysym)
    label.config(text=event.keysym)

def mymouse(event):
    print('Mouse co-ordinate:', str(event.x), str(event.y))

#code

#key events
#the bind represents how tkinter response to every key on the keyboard
#there are two arguments in the bind function ie event &  function
#root.bind(events, function)
#keyboard function
root.bind('<Key>', mykey)
label = tk.Label(root, text='Any key you press will show up here', font=('Arial', 18))
label.pack()

#mouse events
root.bind('<Button-1>', mymouse) #left mouse click
root.bind('<Button-2>', mymouse) #scroll wheel 
root.bind('<Button-3>', mymouse) #right mouse click
root.bind('<ButtonRelease>', mymouse) #event happens after button is released
root.bind('<Enter>', mymouse) #enter the window
root.bind('<Leave>', mymouse) #leave the window
root.bind('<Motion>', mymouse) #occurs when the mouse moves in the window


root.mainloop()