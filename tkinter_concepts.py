import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Registration Form")

# Set the window size
root.geometry("500x400")

# Set the background color to green
root.configure(bg='green')

# Create the input labels and fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

course_label = tk.Label(root, text="Course:")
course_label.pack()
course_entry = tk.Entry(root)
course_entry.pack()

semester_label = tk.Label(root, text="Semester:")
semester_label.pack()
semester_entry = tk.Entry(root)
semester_entry.pack()

form_no_label = tk.Label(root, text="Form No:")
form_no_label.pack()
form_no_entry = tk.Entry(root)
form_no_entry.pack()

contact_no_label = tk.Label(root, text="Contact No:")
contact_no_label.pack()
contact_no_entry = tk.Entry(root)
contact_no_entry.pack()

email_id_label = tk.Label(root, text="Email ID:")
email_id_label.pack()
email_id_entry = tk.Entry(root)
email_id_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Define the function to handle the form submission
def submit_form():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_no = form_no_entry.get()
    contact_no = contact_no_entry.get()
    email_id = email_id_entry.get()
    address = address_entry.get()

    # Do something with the user input (e.g. save to a file or database)
    print("Name:", name)
    print("Course:", course)
    print("Semester:", semester)
    print("Form No:", form_no)
    print("Contact No:", contact_no)
    print("Email ID:", email_id)
    print("Address:", address)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
root.mainloop()



#practice problems
import tkinter as tk
root=tk.Tk() #parent widget
button=tk.Button(root,text='stop',width=25,command=root.destroy)
button.pack() #this helps to organize the widgets in the blocks before placing the parent widget
root.mainloop()

import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text='Hello tkinter')
label.pack()
root.mainloop()

import tkinter as tk
root=tk.Tk()
root.title("Counting method")
button=tk.Button(root,text='count',width=25,command=root.destroy)
button.pack()
root.mainloop()

#creating the messgae box Butoon widget
import tkinter as tk
from tkinter import messagebox
def hello():  #we defined a command 
    msg=messagebox.showinfo("GUI command","button press")
root=tk.Tk()
root.geometry(200*200)  #specifies the word length appearing tkinter
button=tk.Button(root,text="msgbox open",width=25,command=hello)   #command=hello will appaer after clikcing msg box,command=to call function
button.place(50,50)
button.pack()
root.mainloop()

import tkinter as tk
from tkinter import messagebox
def hello():
    msg=messagebox.showinfo("GUI event demo",t.get())
root=tk.Tk()
root.geometry("200x200")
l1=tk.Label(root,text="Name: ")
l1.grid(row=0)
t=tk.Entry(root)
t.grid(row=0,column=1)
button=tk.Button(root,text="To fire click here",width=25,command=hello)
button.grid(row=1,columnspan=2)
root.mainloop() 

import tkinter as tk
from tkinter import messagebox
def hello():
    msg=messagebox.showinfo("GUI command",t.get())
root=tk.Tk()
root.geometry("200x200")
label1=tk.Label(root,text='Name: ')
label1.grid(row=0)
t=tk.Entry(root)
t.grid(row=0,column=1)
button=tk.Button(root,text='Please click here to fire',command=hello)
button.grid(row=1,columnspan=2)
root.mainloop()

#demo of the canva loop
import tkinter as tk
from tkinter import *
root=Tk()
C=Canvas(root,width=40,height=60)
C.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
C.create_line(0,y,canvas_width,y)
mainloop()

#creating a arc based on the canvas and colouring it
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=Tk()  #create parent calss as root
C=Canvas(root,bg="blue",width=250,height=300)  #now create canvas and keep background colour as blue and set width and height
line=C.create_line(10,10,200,200,fill='white') #create line and fill white color
coord=10,50,240,210  #cord means the intersects of all these
arc=C.create_arc(coord,start=0,extent=150,fill='red')   #arc will start from 0 to 150 and it creates arc with color red
C.pack()
root.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=tk.Tk()
C=Canvas(root,bg="blue",width=250,height=300)
line=C.create_line(10,10,200,200,fill="white")
coord=10,50,210,240
arc=C.create_arc(coord,start=0,extent=150,fill="red")
C.pack()  #it will pack up all the commands which we have created 0
root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=tk.Tk()
C=Canvas(root,bg="red",width=250,height=300)
line=C.create_line(10,20,100,200,fill="blue")
C.pack()
root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=tk.Tk()
c=Canvas(root,bg='red',width=250,height=300)
coord=10,50,210,250
arc=c.create_arc(coord,start=0,extent=150,fill='blue')
c.pack()
root.mainloop()

#demonstrating of check button
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def test():
    if(v1.get()==1):
        v2.set(0)
        print("male")
    if(v2.get()==1):
        v1.set(0)
        print("Female")
root=tk.Tk()
root.title("Checkbutton demo")
v1=IntVar()
v2=IntVar()
cb1=Checkbutton(root,text="Male",variable=v1,onvalue=1,offvalue=0,command=test)
cb1.grid(row=0)
cb2=Checkbutton(root,text="Female",variable=v2,onvalue=1,offvalue=0,command=test)
cb2.grid(row=1)
root.mainloop()

#demonstrating the radio button
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def choice():
    if(radio.get()==1):
        root.configure(background="red")
    elif(radio.get()==2):
        root.configure(background="Blue")
    elif(radio.get()==3):
        root.configure(background="green")
root=tk.Tk()
root.geometry("200x200")
radio=IntVar()
rb1=Radiobutton(root,text="Choice 1",variable=radio,width=25,value=1,command=choice)
rb1.grid(row=0)
rb2=Radiobutton(root,text="choice 2",variable=radio,width=25,value=2,command=choice)
rb2.grid(row=1)
rb3=Radiobutton(root,text="Choice 3",variable=radio,width=25,value=3,command=choice)
rb3.grid(row=2)
root.mainloop()


#demonstration of scale
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def slide():
    msg=messagebox.showinfo("Gui event demo",v.get())
root=tk.Tk()
root.geometry("200x200")
root.title("scale event demo")
v=DoubleVar()
scale=Scale(root,variable=v,from_=1,to =50,orient=HORIZONTAL)
scale.pack(anchor=CENTER)
button=Button(root,text="click here to check the value",command=slide)
button.pack(anchor=CENTER)
root.mainloop()