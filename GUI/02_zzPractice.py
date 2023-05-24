import tkinter as tk

class myclass:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Practice")
        self.root.geometry('500x590')

        #Menu
        #------------------------------------------
        self.Nav = tk.Menu(self.root)

        self.m1 = tk.Menu(self.Nav, tearoff=0)
        self.Nav.add_cascade(menu=self.m1, label='Load')
        self.m1.add_command(label='ASCI')
        self.m1.add_command(label='Text')
        self.m1.add_command(label='CSV')
        self.m1.add_command(label='xlcl')

        self.m2 = tk.Menu(self.Nav, tearoff=0)
        self.Nav.add_cascade(menu=self.m2, label='Graph')
        self.m2.add_command(label='Log Graph')
        self.m2.add_command(label='Histogram')
        self.m2.add_command(label='Normal Distribution')

        self.m3 = tk.Menu(self.Nav, tearoff=0)
        self.Nav.add_cascade(menu=self.m3, label='Analysis')

        self.m4 = tk.Menu(self.Nav, tearoff=0)
        self.Nav.add_cascade(menu=self.m4, label='Report')

        self.m5 = tk.Menu(self.Nav, tearoff=0)
        self.Nav.add_cascade(menu=self.m5, label='AI Bolt')
        self.m5.add_command(label='chatGPT openAI')

        self.root.config(menu=self.Nav)
        #-------------------------------------------

        self.intro = tk.Label(self.root, text='SCHEDULE PLAN & BUDGET', font=(10))
        self.intro.pack(padx=20, pady=20)


        self.fed = tk.Label(self.root, text='We appreciate feedbacks. Please leave us some, THANK YOU')
        self.fed.pack(padx=20, pady=0)
        self.textC = tk.Text(self.root)
        self.textC.pack(padx=30, pady=30)

        self.email = tk.Button(self.root, text='Send Email', command=self.send_mail)
        self.email.pack(padx=10, pady=10)



        self.root.mainloop()

    def send_mail(self):
        print(self.textC.get('1.0', tk.END))

myclass()