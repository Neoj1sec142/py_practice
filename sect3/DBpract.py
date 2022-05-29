import mysql.connector
# myDB = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "this1503")

myDB = mysql.connector.connect(user='root', passwd='this1503',
                              host="localhost", database='python_X',
                              
                              )


print(myDB)
# myDB.close()