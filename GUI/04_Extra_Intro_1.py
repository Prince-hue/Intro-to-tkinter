import tkinter as tk

root=tk.Tk()

#scales
scale = tk.Scale(root, 
                 from_=0, 
                 to=100,
                 length=600,
                 orient='vertical', #oreintation can horizontal. it is vertical by default
                 tickinterval=10, #numeric indicators on the scale
                 #showvalue=0 --hides current value
                 troughcolor='#69FAFF',
                 fg='#ff1c00',
                 bg='#111111'
                 )
#starting at 37 instead of 0
scale.set(37)
scale.pack()

scale_btn = tk.Button(root, text='Current Temperature in degree celcius', command=lambda: scaleValue())
scale_btn.pack()

#functions --------------------------------------------
def scaleValue():
    print('The temperature is', scale.get(), 'degree celcius')

root.mainloop()