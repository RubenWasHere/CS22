from tkinter import *
import tkinter.font, random, re

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master, ...)
        self.grid()
        self.create_widgets()
        self.start()

        
    def parse(self):
        ...


    def create_widgets(self):
        
        ...

        self.submit = Button(self, text= "Submit Command.", command= self.parse, ...)
        self.submit.grid(...)

        
root = Tk()
root.bind('<Return>', self.parse)

app = Application(root)

root.mainloop()
