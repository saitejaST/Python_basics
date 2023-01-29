from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

Label=Label(root,front=("ds-digital",80),background="blue",foreground="cyan")
Label.pack(anchor='center')
time()

mainloop()
