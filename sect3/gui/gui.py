# First GUI Window
from tkinter import *
from PIL import Image, ImageTk
window = Tk()

img = Image.open('python.png')
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

button = Button(window, text='Lets Start')

username = Label(window, text='Username', font=('Serif', 12))
inputBox = Entry(window)

name = Label(window, text="PythonX - Learn Python", bg='white', fg='Blue', font=("Serif", 16))
name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.place(x=100, y=180)

window.mainloop()

