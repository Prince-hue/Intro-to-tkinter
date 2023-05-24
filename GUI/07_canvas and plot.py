import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np
import pandas as pd

def plot():
    #generate random data
    ax.clear()
    x = training_file['GR'] #np.random.randint(0, 10, 10) #btn  0 to 10 , 10 random numbers
    y = training_file['DEPTH']
    #x =np.random.randint(0, 10, 10) #btn  0 to 10 , 10 random numbers
    #y =np.random.randint(0, 10, 10) #btn  0 to 10 , 10 random numbers
    #ax.scatter(x,y)
    ax.plot(x,y)
    #plt.show()
    canvas.draw()

root = tk.Tk()
rootimg = tk.PhotoImage(file='logo.png')
root.iconphoto(True, rootimg)

training_file = pd.read_csv('C:\\Users\\pc\\Desktop\\BD_ML App\\trainfile.csv')
        

#create matplot figure
fig, ax = plt.subplots()

#frame--------------------
frame = tk.Frame(root)
label = tk.Label(frame, text='Matplotlib + tkinter', font=('Courier', 20))
label.pack()
#create canvas
canvas = FigureCanvasTkAgg(fig, master=frame)
#how to pack() a canvas 
canvas.get_tk_widget().pack()

#to add navigation to the plots
toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor = 'w', fill=tk.X)

frame.pack()
#------------------------------------------

tk.Button(frame, text='Plot Graph', command=plot).pack(pady=10)
root.mainloop()