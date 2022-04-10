import tkinter as tk
from tkinter import ttk

root = tk.Tk()
months = tk.StringVar()

Combobox = ttk.Combobox(root, textvariable=months,
                            values = ('Jan', 'Feb', 'Mar', 'Apr'),
                            state='readonly').grid(row=6, column=0)

root.geometry('500x450')
root.mainloop()