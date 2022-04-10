import tkinter as tk
from tkinter import Spinbox, StringVar, ttk


root = tk.Tk()


# create spinbox - 'from' is a special keyword for Python - #
# so we need to use _ after it
year = StringVar()
Spinbox(root,from_ = 1989, to = 2022, textvariable = year).grid(row=6,column=1)

root.geometry('500x450')
root.mainloop()

