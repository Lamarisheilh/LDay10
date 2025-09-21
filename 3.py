from tkinter import *

master = Tk()
master.title("tk")
master.geometry("200x50")

w = Label(master, text='First Name')
w.grid(row=0)

w = Label(master, text='Last Name')
w.grid(row=1)

w = Entry(master)
w.grid(row=0, column=1)

w = Entry(master)
w.grid(row=1, column=1)

mainloop()