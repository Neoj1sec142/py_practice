# Employee CRUD App:
### Tech Used:
refer to password with os.environ.get('PASSWD') - to process .env

* mysql
* python
* tkinter
### Database Creation:
```sh 
CREATE DATABASE employee;
# Check With:
SHOW DATABASES;
```
### empDetails Table Creation:
```sh 
CREATE TABLE empDetails(empID int PRIMARY KEY, empName varchar(100), empDept varchar(100));
```