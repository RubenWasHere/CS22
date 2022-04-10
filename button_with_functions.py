from tkinter import * #imports everything from TK

root = Tk() #top level window

def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')

# added font colour and background 

# colour on click

# create label
label = Label(root, text="Hello Python")
label.pack()

# create button(now with the comannad function
button = Button(root, text='Click Me!', command=callback)
button ['state'] ='disabled' # can disable the button
button ['state'] ='normal' # back to normal
button.pack()

root.geometry("350x300")
root.mainloop()

