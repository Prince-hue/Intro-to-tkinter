import tkinter as tk
root = tk.Tk()



#canvas --it is a widget use to draw graphs, plots, images in a window
canvas = tk.Canvas(root, height=500, width=500)
#shapes
canvas.create_line(0,0,500,500, #x1, y1, x2, y2 where (x1,y1) = starting pt
                   fill='blue',
                   width=5)
rec_cord = [50, 50, 250, 250]
canvas.create_rectangle(rec_cord,
                        fill='purple')
canvas.create_polygon(250, 0, 0, 500, 500, 500, #the more the co-ordinates, the higher the number of sides increase
                        fill='yellow', 
                        outline='black',
                        width=5)
canvas.pack()


root.mainloop()