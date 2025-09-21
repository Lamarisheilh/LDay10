import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
r.geometry("400x100")

w = tk.Button(r, text='Stop', width=25, command=r.destroy)
w.pack()

r.mainloop()