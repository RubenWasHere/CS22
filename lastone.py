from tkinter import *
from tkinter import ttk # sun module of tkiner with more widgets

root = Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("your name is :" + val1)
    print("your password is :" + val2)

Label1 = Label(root, text="Name ")
Label2 = Label(root, text="Password ")

#create entry boxes
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0,"")
entry2.config(show="*")


#add a button to the window
button=ttk.Button(root,text="cool button", command=callback)

Label1.pack()
entry.pack()
Label2.pack()
entry2.pack()
button.pack()


root.geometry("300x300") # the size of the widnow
root.mainloop()