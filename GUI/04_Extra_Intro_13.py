import tkinter as tk
from time import *

def update():
    #return current time and format it
    time_s = strftime('%I:%M:%S %p') #this converts tuple to string as time %M -minute, %S -seconds etc..
    time.config(text=time_s) #displays current time
    day_s = strftime('%A') #day of the week
    day.config(text=day_s) #date of the day
    date_s = strftime('%B %d %Y')
    date.config(text=date_s)
    #update root every 1000 millisecond = 1 sec
    root.after(1000, update) #two arguments - the delay , - we call the function in itself (recursive function)

root = tk.Tk()

#creating a clock
time = tk.Label(root, font=('Arial', 18), fg='#00ff00', bg='black')
time.pack()
day = tk.Label(root, font=('Ink Free', 18))
day.pack()
date = tk.Label(root, font=('Ink Free', 18))
date.pack()

#update time every 1 sec 
update()


root.mainloop()