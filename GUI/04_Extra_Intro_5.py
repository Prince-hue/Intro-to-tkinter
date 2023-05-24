import tkinter as tk
#progress bar is found in ttk, so
from tkinter import ttk
import time
root = tk.Tk()

#function
def start():
    GB = 1000 #10 GBs
    upload = 0  #0/10 GB done
    Kb_s = 2
    while (upload<GB):
        time.sleep(1) #delay -- we wait 1 sec after the progress bar completees, then it displays
        bar['value']+=(Kb_s/GB)*100
        upload+=Kb_s
        #r.set(str((upload/GB)*100)+'%') --use this to leave the r in decimals
        r.set(str(int((upload/GB)*100))+'%')
        t.set(str(upload)+' / '+str(GB)+' GB completed')
        root.update_idletasks() #this updates the progress bar after each iteration, hence we see a 1 sec delay progression of the bar

    #bar['value']+=10 #progress bar get filled by 0.1 after every tab of the upload btn


#grids
label = tk.Label(root,text='ENTER BIO INFO', font=('Arial', 30))
label.grid(row=0, columnspan=2)

label_f = tk.Label(root,text='First Name')
label_f.grid(row=1, column=0)
entrybox_f = tk.Entry(root)
entrybox_f.grid(row=1, column=1)

label_l = tk.Label(root,text='Last Name')
label_l.grid(row=2, column=0)
entrybox_l = tk.Entry(root)
entrybox_l.grid(row=2, column=1)
#columnspan=2 means say merging two column cells in excel
submit_btn = tk.Button(root, text='Submit').grid(row=3, columnspan=1) 

#Progress Bar
label_p = tk.Label(root,text='Progress Bar', font=('Arial', 30))
label_p.grid(row=4, columnspan=2)
tk.Button(root, text='Upload', command=lambda: start()).grid(row=5, column=0, columnspan=2)
bar = ttk.Progressbar(root, orient='horizontal', length=300)
bar.grid(row=6, columnspan=2)
r = tk.StringVar() #we define the textvarible
t = tk.StringVar()
update_percent = tk.Label(root, textvariable= r)
update_percent.grid(row=7,column=1)
update_GB = tk.Label(root, textvariable= t).grid(row=8,column=1)


root.mainloop()