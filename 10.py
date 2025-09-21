from tkinter import *

master = Tk()

w = Scale(master, from_=0, to=30)
w.pack()

w = Scale(master, from_=0, to=200, orient="vertical")

w.pack()
mainloop()