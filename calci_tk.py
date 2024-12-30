from tkinter import *
window=Tk()
#Addition
def add():
    x=float(e1.get())
    y=float(e2.get())
    l3.config(text=f"Answer:{x+y}")
    # return x+y
#Subtraction
def sub():
    x=float(e1.get())
    y=float(e2.get())
    l3.config(text=f"Answer:{x-y}")
    # return x-y
#Multiplicaion
def mul():
    x=float(e1.get())
    y=float(e2.get())
    l3.config(text=f"Answer:{x*y}")
    # return x*y
#division
def div():
    x=float(e1.get())
    y=float(e2.get())
    l3.config(text=f"Answer:{x/y}")
    # return x/y
window.title("Calculator")
window.geometry("400x200")
l1=Label(window,text="Enter Value 1",fg="green")
l1.place(x=0,y=20)
e1=Entry(window,width=50)
e1.place(x=100,y=20)
l2=Label(window,text="Enter Value 2",fg="green")
l2.place(x=0,y=70)
e2=Entry(window,width=50)
e2.place(x=100,y=70)
b1=Button(window,text="Add",command=add)
b1.place(x=0,y=120)
b2=Button(window,text="Substract",command=sub)
b2.place(x=50,y=120)
b3=Button(window,text="Multiply",command=mul)
b3.place(x=120,y=120)
b4=Button(window,text="Divide",command=div)
b4.place(x=190,y=120)
l3=Label(window,text="Answer")
l3.place(x=0,y=150)

window.mainloop()

