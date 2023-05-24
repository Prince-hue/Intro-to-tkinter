import tkinter as tk
root = tk.Tk()
root.title('TUTORIAL')
root.geometry('300x500')

btn = tk.Button(root, text='Click')
btn.pack(padx=10, pady=30)

btnC = tk.Frame(root)
btnC.columnconfigure(0, weight=3)
btnC.columnconfigure(1, weight=1)
btnC.columnconfigure(2, weight=1)
btnC.columnconfigure(3, weight=1)
btnC.columnconfigure(4, weight=1)

btnCn1 = tk.Button(btnC, text = 'sq rt')
btnCn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btnCn2 = tk.Button(btnC, text = 'sq rt')
btnCn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btnCn3 = tk.Button(btnC, text = 'sq rt')
btnCn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btnCn4 = tk.Button(btnC, text = 'sq rt')
btnCn4.grid(row=0, column=3, sticky=tk.W+tk.E)

btnCn5 = tk.Button(btnC, text = 'sq rt')
btnCn5.grid(row=0, column=4, sticky=tk.W+tk.E)

#------------------------------------------------

btnCn6 = tk.Button(btnC, text = 'sq rt')
btnCn6.grid(row=1, column=0, sticky=tk.W+tk.E)

btnCn7 = tk.Button(btnC, text = 'sq rt')
btnCn7.grid(row=1, column=1, sticky=tk.W+tk.E)

btnCn8 = tk.Button(btnC, text = 'sq rt')
btnCn8.grid(row=1, column=2, sticky=tk.W+tk.E)

btnCn9 = tk.Button(btnC, text = 'sq rt')
btnCn9.grid(row=1, column=3, sticky=tk.W+tk.E)

btnCn10 = tk.Button(btnC, text = 'sq rt')
btnCn10.grid(row=1, column=4, sticky=tk.W+tk.E)

btnC.pack(fill='x')

root.mainloop()