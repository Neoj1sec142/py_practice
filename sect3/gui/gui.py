# First GUI Window
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


# USING the Command Option
def gui():
    window = Tk()

    name = Label(window, text="PythonX - Learn Python", bg='white', fg='Blue', font=("Serif", 16))
    img = Image.open('python.png')
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)
    frame = Frame(window)
    username = Label(frame, text='Username', font=('Serif', 12))
    inputBox = Entry(frame)
    button = Button(window, text='Lets Start', command=showMessage)
    
    # greet = Label(window)

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack(side=BOTTOM)
    # greet.pack()
    window.mainloop()

def showMessage():
    messagebox.showinfo("PythonX - Learn Python", 'Welcome')
if __name__ == '__main__':
    gui()

# Using the BIND function
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox

# def greetUser():
#     username = inputBox.get()
#     greet['text'] = 'Welcome' + username
#     window = Tk()
#     name = Label(window, text="PythonX - GUI with Bind", bg='white', fg='Blue', font=('Serif', 16))
#     img = Image.open('python.png')
#     logo = ImageTk.PhotoImage(img)
#     image = Label(window, image=logo)
#     frame = Frame(window)
#     username = Label(frame, text='Username', font=('Serif', 12))
#     inputBox = Entry(frame)
#     button = Button(window, text='Lets Start')
#     button.bind('<Button>', greetUser)
#     greet = Label(window)
#     name.pack()
#     image.pack()
#     frame.pack() 
#     username.pack(side=LEFT)
#     inputBox.pack(side=RIGHT)
#     button.pack()
#     greet.pack()
#     window.mainloop()

# We have added our GUI code into a function called gui() just to format the code better,
# the gui() is then called in the main section in the special variable name
# we have simply defined a method called showMessage() that shows a message box
# finally, in the button, we add the command option and pass the name of the handler method as value #