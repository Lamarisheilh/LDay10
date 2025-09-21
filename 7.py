from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(50):
    mylist.insert(END, 'This is line number' + str(line+1))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()