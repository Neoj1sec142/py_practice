
from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as con

window = Tk()
window.geometry("600x270")
window.title("PyTk/MySQL CRUD App")


empID = Label(window, text="Employee ID", font=("Serif", 12))
empID.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif", 12))
empDept.place(x=20, y=90)

enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

def insertData():
    # Read the data provided by the user
    Id = enterId.get()
    nm = enterName.get()
    dept = enterDept.get()
    if(Id == '' or nm == "" or dept == ""):
        mb.showwarning("Cannot Insert", "All Fields Required")
    else:
        myDB = con.connect(host='localhost', user='root', passwd='thisguy142', database='employee', auth_plugin='mysql_native_password')
        myCur = myDB.cursor()
        myCur.execute("INSERT INTO employee.empDetails (empID,empName,empDept) VALUES (%s,%s,%s)", (Id, nm, dept));
        myDB.commit()
        enterId.delete(0, 'end')
        enterName.delete(0, 'end')
        enterDept.delete(0, 'end')
        mb.showinfo("Insert Status", "Data Interted Successfully")
        myDB.close()

insertBtn = Button(window, text="Insert", font=("Sans", 12), bg="white", command=insertData)
insertBtn.place(x=20,y=160)

# content in command =  needs to be un quoted after functions are built
updateBtn = Button(window, text="Update", font=("Sans", 12), bg="white", command="updateData")
updateBtn.place(x=80,y=160)

getBtn = Button(window, text="Get", font=("Sans", 12), bg="white", command="getData")
getBtn.place(x=150,y=160)

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg="white", command="deleteData")
deleteBtn.place(x=210,y=160)

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white", command="resetData")
resetBtn.place(x=20,y=210)

showData = Listbox(window)
showData.place(x=330, y=30)

window.mainloop()