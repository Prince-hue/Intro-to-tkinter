import tkinter as tk
#imports a message box
from tkinter import messagebox
#imports color chooser
from tkinter import colorchooser

root=tk.Tk()

#list
list = tk.Listbox(root, width=22, font='Constantia', bg='#f7ffde', 
                  selectmode='multiple' #allows for multiple selection
                  ) 
list.pack()
list.insert(0, 'PDF')
list.insert(1, 'DOC')
list.insert(2, 'XLSL')
list.insert(3, 'CSV')
#removes the extra spaces created by the list box
list.config(height=list.size())
#create entry for user to update list
update_list = tk.Entry(root)
update_list.pack()
list_add = tk.Button(root, text='Update list', command= lambda: add_to_list()).pack()
list_del = tk.Button(root, text='Remove single item from list', command= lambda: remove_from_list()).pack()
list_del_m = tk.Button(root, text='Remove multiple items from list', command= lambda: del_multiple_selection()).pack()
#create button under list to submit
list_btn = tk.Button(root, text='submit', command=lambda: submit_list())
list_btn.pack()

#message box
msg_btn = tk.Button(root, text='click me to see message box', command= lambda: msg()).pack()

#color_viewer
color_btn = tk.Button(root, text='Select Color', command= lambda: color_picker())
color_btn.pack()

#text widget
textarea = tk.Text(root,
                   bg= '#00ffff',
                   font=('Ink Free', 18),
                   padx=5,
                   pady=5, 
                   height=10,
                   width=50
                   )
textarea.pack()
btn_text = tk.Button(root, command= lambda: submit_text(), text='Submit Comment')
btn_text.pack()

#functions --------------------------------------------
def submit_list():
    #list_m = [] --This would submit multiple items
    #for i in list.curselection():
        #list_m.insert(i, list.get(i))
    print('You have requested for', list.get(list.curselection()), 'file')

def add_to_list():
    list.insert(list.size(), update_list.get())
    list.config(height=list.size())

def remove_from_list():
    print('You have deleted', list.get(list.curselection()), 'file')
    list.delete(list.curselection())
    list.config(height=list.size())

def del_multiple_selection():
    for i in reversed(list.curselection()):
        list.delete(i)

def msg():
    messagebox.showinfo(title='Facts and Hacks', message='Did you know that candles don\'t cast shadows ?')

    #while(True):
        #messagebox.askokcancel(title='Prompt', message= 'Do you want to save changes ?')

    ans = messagebox.askquestion(title='Prompt', message= 'Do you want to exit while program is still running ?')
    if (ans == 'yes'):
        messagebox.showinfo(message='Progress will be lost')
    else:
        messagebox.showinfo(message='Saving...')

    if (messagebox.askokcancel(title='Prompt', message= 'Do you want to save changes ?')):
        messagebox.showinfo(message='File is saved')
    else:
        messagebox.showinfo(message='File is left unsaved. All progress is lost')

    #print(messagebox.askyesnocancel(message='Are you enjoying coding ?'))
    answer = messagebox.askyesnocancel(message='Are you enjoying coding ?')
    if (answer == True):
        messagebox.showinfo(message='Great, I also love coding :)')
    elif (answer == False):
        messagebox.showinfo(message='Gee, and I thought we were getting along :(')
    elif (answer == None):
        messagebox.showerror(message='Are you avoiding me ?')

def color_picker():
    get_color = colorchooser.askcolor()
    print(get_color)
    #to extract hex decimal value from the array printed, we use the second index, ie 1
    hex = get_color[1]
    print(hex)
    root.config(bg=hex) #this will change background color upon color picker selector

def submit_text():
    get_text = textarea.get('1.0', tk.END)
    print(get_text)
    


root.mainloop()