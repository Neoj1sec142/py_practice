import os
from tkinter import *
from tkinter import messagebox as mb
from .operations import *

win = Tk()
win.geometry("600x270")
win.title("Calculator")

output = None

ipt1 = Label(win, text='Input 1: ', font=("Serif", 12))
ipt1.place(x=20, y=30)

ipt2 = Label(win, text='Input 2: ', font=("Serif", 12))
ipt2.place(x=20, y=60)

enterI1 = Entry(win)
enterI1.place(x=170, y=30)
enterI2 = Entry(win)
enterI2.place(x=170, y=60)

def resetData():
    enterI1.delete(0, "end")
    enterI2.delete(0, "end")
    global output = None
    

resetBtn = Button(win, text="Reset", font=("Sans", 12), bg="white", command=resetData)
resetBtn.place(x=20,y=210)

def multiply(n1, n2):
    if n1 == None or n2 == None:
        mb.showwarning("Please input 2 numbers to multiply")
    else:
        
        return output

mltpyBtn = Button(win, text="X", font=("Sans", 12), bg="white", command="resetData")
mltpyBtn.place(x=50,y=160)

dvdBtn = Button(win, text="/", font=("Sans", 12), bg="white", command="resetData")
dvdBtn.place(x=100,y=160)

addBtn = Button(win, text="+", font=("Sans", 12), bg="white", command="resetData")
addBtn.place(x=150,y=160)

subBtn = Button(win, text="-", font=("Sans", 12), bg="white", command="resetData")
subBtn.place(x=210,y=160)

def show():
    showData.delete(0, showData.size())
    showData.insert(showData.size()+1, output)

showData = Listbox(win)
showData.place(x=350, y=30)
show()
win.mainloop()