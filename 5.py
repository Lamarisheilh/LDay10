from tkinter import *

root = Tk()
root.title("-")

v = IntVar()

Radiobutton(root, text='GfG', variable=v, value=1).grid(row=0, column=0)
Radiobutton(root, text='MIT', variable=v, value=2).grid(row=0, column=1)

mainloop()