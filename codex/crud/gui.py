import os
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
        myDB = con.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='employee', auth_plugin='mysql_native_password')
        myCur = myDB.cursor()
        myCur.execute("INSERT INTO employee.empDetails (empID,empName,empDept) VALUES (%s,%s,%s)", (Id, nm, dept));
        myDB.commit()
        enterId.delete(0, 'end')
        enterName.delete(0, 'end')
        enterDept.delete(0, 'end')
        show()
        mb.showinfo("Insert Status", "Data Interted Successfully")
        myDB.close()

insertBtn = Button(window, text="Insert", font=("Sans", 12), bg="white", command=insertData)
insertBtn.place(x=20,y=160)

def updateData():
    id = enterId.get()
    nm = enterName.get()
    dept = enterDept.get()
    if(id=="" or nm=="" or dept==""):
        mb.showwarning("Cannot Update", "All Fields Required")
    else:
        myDB = con.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='employee', auth_plugin='mysql_native_password')
        myCur = myDB.cursor()
        myCur.execute("UPDATE empDetails set empName=%s,empDept=%s where empID=%s", (nm, dept, id))
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        show()
        mb.showinfo("Update Status:", "Data Updated Successfully")
        myDB.close()

updateBtn = Button(window, text="Update", font=("Sans", 12), bg="white", command=updateData)
updateBtn.place(x=80,y=160)

def getData():
    if(enterId.get() == ""):
        mb.showwarning("Fetch Status:", "Please Enter the ID of the Employee You Are Looking For.")
    else:
        myDB = con.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='employee', auth_plugin='mysql_native_password')
        myCur = myDB.cursor()
        myCur.execute("SELECT * FROM empDetails where empID="+enterId.get()+"")
        rows = myCur.fetchall()
        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
        # mb.showinfo("")
        myDB.close()

getBtn = Button(window, text="Get", font=("Sans", 12), bg="white", command=getData)
getBtn.place(x=150,y=160)

def deleteData():
    if(enterId.get() == ""):
        mb.showwarning("Please provide the Id of the employee you want to remove.")
    else:
        myDB = con.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='employee', auth_plugin='mysql_native_password')
        myCur = myDB.cursor()
        myCur.execute("DELETE FROM empDetails where empID="+enterId.get()+"")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        show()
        mb.showinfo("Delete Status:", "Data Deleted Successfully")
        myDB.close()

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg="white", command=deleteData)
deleteBtn.place(x=210,y=160)

def resetData():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white", command=resetData)
resetBtn.place(x=20,y=210)

def show():
    myDB = con.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='employee', auth_plugin='mysql_native_password')
    myCur = myDB.cursor()
    myCur.execute("SELECT * FROM empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())
    for row in rows:
        addData = str(row[0])+' '+row[1]+' '+row[2]
        showData.insert(showData.size()+1, addData)
    myDB.close()

showData = Listbox(window)
showData.place(x=330, y=30)
show()
window.mainloop()