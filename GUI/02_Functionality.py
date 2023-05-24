import tkinter as tk
#allows for the execution of a message box
from tkinter import messagebox

#Creating a class
class MyGUI:
     #Creating a function
     def __init__(self):

          #Creating a window in tkinter
          self.root = tk.Tk()

          #how to add menu bars into the widget
          self.menubar = tk.Menu(self.root)

          #a menubar extention of the first menubar --ie the widget is not attached to self.root
          #the tearoff removes a dashline at the top
          self.filemenu = tk.Menu(self.menubar, tearoff=0)
          #the name of the command is close n what it does is to exit out of the window
          self.filemenu.add_command(label='Close', command=exit)
          #making it block so that they are not in_line
          self.filemenu.add_separator()
          #adding another command to the filename menubar
          self.filemenu.add_command(label='Close with Prompt', command=self.on_closing)

          #adding another menubar
          self.actionmenu = tk.Menu(self.menubar, tearoff=0) 
          self.actionmenu.add_command(label='Show Message', command=self.show_message)

          #adding to the menubar to filemenu
          self.menubar.add_cascade(menu=self.filemenu, label='File')
          self.menubar.add_cascade(menu=self.actionmenu, label='Action')
          #adding the menubar to the root
          self.root.config(menu=self.menubar)


          #Adding a label widget
          self.label = tk.Label(self.root, text='Your Message', font=('Arial', 18))
          self.label.pack(padx=10, pady=10)

          #Adding a textbox widget
          self.textbox = tk.Text(self.root, height=5, font=('Arial', 19))
          #how to assign a key to execute a task-- we bind a fxn called shortcut to the textbox
          self.textbox.bind('<KeyPress>', self.shortcut)
          self.textbox.pack(padx=10, pady=10)

          #Creating a variable for the checkbox
          self.check_state = tk.IntVar()
          #Adding a check widget
          self.check = tk.Checkbutton(self.root, text='Show Message', font=('Arial', 16), variable=self.check_state)
          self.check.pack(padx=10, pady=10)

          #Adding a button widget
          self.button = tk.Button(self.root, text='Message', command=self.show_message)
          self.button.pack(padx=30, pady=20)

          #Clearing the textbox of any text
          self.clearbtn = tk.Button(self.root, text='Clear', font=('Arial', 18), command=self.clear)
          self.clearbtn.pack(padx=10, pady=10)

          #To get a message when tk window is closed, we use protocol 
          self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
          #End of tkinter window
          self.root.mainloop()

     #This command prints the message into the terminal. Use to check if the code is working
     #def show_message(self):
     #     print("Prince is your name")

     #Creating a function that checks if the state of the checkbox is checked
     def show_message(self):
          #print(self.check_state.get()) --This prints out 0s and 1s whenever the checkbox is check or not
          #Since the checkbox is 0 when unchecked and 1 when checked we assign a state to the checkbox
          if self.check_state.get()== 0:
               #'1.0' is a string for start & tk.END is for end if u want to get everything
               print(self.textbox.get('1.0', tk.END))
          else:
               #else we import a message box with the message it contains
               messagebox.showinfo(title='Message', message= self.textbox.get('1.0', tk.END))

     def shortcut(self, event):
          #events prints out the state, keysym & keycode of the key triggered 
          #print(event)
          #print(event.keysym)
          #print(event.state)

          # 12 is the state when Ctrl is triggered and Return is the keysym when Enter is triggered
          if event.state == 12 and event.keysym == 'Return':
               #This executes the code into the terminal when ctrl + Enter is triggered without checking the box
               #The Ctrl + Enter prints the message into the message box when the checkbox is checked
               self.show_message()

     #Creating a function that displays a message when the close button is triggered
     def on_closing(self):
          #Calls out the ask yes & no to execute a program
          if messagebox.askyesno(title='Quit', message = 'Do you really want to quit ?'):
               #prints out into the terminal when the close button is triggered
               #print('Closing...')
               self.root.destroy()

     #Creating a function that clears the text from the textbox
     def clear(self):
          self.textbox.delete('1.0', tk.END)

#Calling / Executing the class
MyGUI()