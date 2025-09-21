from tkinter import *

master = Tk()
master.title("-")
master.geometry("100x50")

w1 = IntVar()
w1 = Checkbutton(master, text='male', variable=w1)
w1.grid(row=0, sticky=W)

w2 = IntVar()
w2 = Checkbutton(master, text='female', variable=w2)
w2.grid(row=1, sticky=W)

mainloop()