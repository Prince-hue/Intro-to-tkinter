import tkinter as tk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(title='Open files',
                                          #initialdir='C://Users//pc//Desktop', --it gives the path an initial directory
                                          filetypes=(('Text files', '.txt'), ('All files', '*.*'))
                                          
                                          )
    
    #creates a variable that stores text from the text area box
    print(filepath) #prints file type
    file = open(filepath, 'r') #r stands for read text file
    print(file.read())
    file.close()

def save_file():
    filesave = filedialog.asksaveasfile(defaultextension='.txt',
                                        initialdir='C://Users//pc//Desktop',
                                        filetypes=[
                                            ('Text file','.txt'),
                                            ('UTF-8 Comma Separated Vectors', '.csv'),
                                            ('PDF','.pdf'),
                                            ('HTML', '.html'),
                                            ('All files', '*.*')
                                        ])
    if (filesave is None):
        return #this would preventing getting a exception error when one quits from the saveas window without saving
    #creates a variable that stores text from the text area box
    text_save_get = str(text_save.get('1.0', tk.END))
    #text_save = input('Enter some text: ') -- text will be entered inside the terminal to be saved
    #we write the text to this file
    filesave.write(text_save_get)
    filesave.close()

def new_window():
    #creates window that doesn't log out after closing root window
    top_win = tk.Tk()
    #destroy the old window
    root.destroy()


#codes --------------------------------------------
root =tk.Tk()

#menubar
nav = tk.Menu(root) #we add a menu bar to our root window
root.config(menu=nav)
#creating separate menu and adding it to the menu bar
menu1 = tk.Menu(nav, tearoff=0)
nav.add_cascade(label='File', menu=menu1)
menu1.add_command(label='Open', command=open_file)
menu1.add_command(label='Save', command=save_file)
menu1.add_separator()
menu1.add_command(label='Exit', command=quit)

#adding img to menu 2
img1 = tk.PhotoImage(file='logo.png', height=20, width=20)#, height=50, width=50)
#creating menu 2
menu2 = tk.Menu(nav, tearoff=0)
nav.add_cascade(label='Edit',menu=menu2)
menu2.add_command(label='Cut', 
                  image=img1, 
                  compound='left') # places img on the left side leaving the text on the right
menu2.add_command(label='Copy')
menu2.add_command(label='Paste')


#filedialog open
btn = tk.Button(root, 
                text='Open', 
                command=open_file
                )
btn.pack()

#filedialog save
btn_save = tk.Button(root, 
                text='Save', 
                command=save_file
                )
btn_save.pack()
text_save = tk.Text(root)
text_save.pack()

#Frame
frame_box = tk.Frame(root,
                     bg='black',
                     bd=5, #border
                     relief='raised', #type of border
                     )
frame_box.pack(side='bottom')
tk.Button(frame_box, text='W', font=('Consolas', 25), width=3).pack(side='top')
tk.Button(frame_box, text='A', font=('Consolas', 25), width=3).pack(side='left')
tk.Button(frame_box, text='S', font=('Consolas', 25), width=3).pack(side='left')
tk.Button(frame_box, text='D', font=('Consolas', 25), width=3).pack(side='left')

#creating a new window
btn1 = tk.Button(root, text='Top Window', command=lambda: tk.Toplevel())#creating a top level window. Close the root window and the top window also closes
btn1.pack()

btn2 = tk.Button(root, text='New Window', command= new_window) 
btn2.pack()




root.mainloop()