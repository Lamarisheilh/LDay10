from tkinter import *
top = Tk()
top.title("-")

Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Java')
Lb.insert(4, 'Any other')
Lb.pack()

top.mainloop()