import tkinter as tk

root = tk.Tk()
root.geometry('920x1020')
root.title('Intro')

#adding img as favicon
favicon = tk.PhotoImage(file='logo.png')
root.iconphoto(True, favicon)

#changing background color
root.config(background='lightblue')

#label
#adding an img to a label
label_img = tk.PhotoImage(file='logo.png')
label = tk.Label(root, 
                 text='label goes here', 
                 font=('Arial', 20, 'bold'), 
                 fg='#00ff00', 
                 bg='green',
                 padx=20,
                 pady=10)
                 #image=label_img,
                 #compound='top' -- position's the image)
label.pack() #--centers widget
#label.place(x=100, y=100) --user specifies coordinates
#label.grid()

#buttons
btn = tk.Button(root, 
                text='Click me', 
                command=lambda: click(),
                font=('Comic Sans', 20),
                fg='blue',
                bg='green',
                activebackground='yellow',
                activeforeground='red')
btn.pack()

#entry box
entry = tk.Entry(root,
                 font=("Arial", 20))
                 #show='*')
entry.pack(side='left')
submit_btn = tk.Button(root, 
                       text='Submit', 
                       command= lambda: submit())
submit_btn.pack(side='right')
del_btn = tk.Button(root, 
                       text='Clear', 
                       command= lambda: clear())
del_btn.pack(side='right')
backspace_btn = tk.Button(root, 
                       text='Back Space', 
                       command= lambda: backspace())
backspace_btn.pack(side='right')

#checkboxes
checked = tk.IntVar()
checkbox = tk.Checkbutton(root, text='Do you consent ?', variable=checked, command=lambda: check())
checkbox.pack()

#radio buttons
#creating a list
food = ['pizza', 'hamburger', 'hotdog']
radio_img = tk.PhotoImage(file='logo.png')
arr_img = [radio_img, radio_img, radio_img]
#this will hold an integer object and make sure that one is selected at a time
x = tk.IntVar()
for index in range(len(food)):
    radiobutton = tk.Radiobutton(root, 
                                 text=food[index], #adds text to radio buttons
                                 variable=x, #groups radiobuttons together if they share the same variable, a different group would take say variable = y
                                 value=index,
                                 padx=0,
                                 font=('Impact', 18),
                                 indicatoron=0, #removes the indicators
                                 width= 373,
                                 command=lambda: radio()) #sets width of radio buttons
                                 #image=arr_img[index])
                                 #compound = 'left' -- adds image and text) #assigns each radiobutton a different value
    radiobutton.pack(anchor='w') #all are now lined up to the west




#functions ----------------------------------------------------------

count=0
def click():
    global count
    count+=1
    print('You clicked this button', count, 'times')

def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state='disabled')

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def check():
    if (checked.get() == 1):
        print('Agreed')
    else:
        print('Disagreed')

def radio():
    if (x.get()==0):
        print('You ordered 1')
    elif (x.get()==1):
        print('You ordered 2')
    elif (x.get()==2):
        print('You ordered 3')
    else:
        print('huh')
    
    
root.mainloop()