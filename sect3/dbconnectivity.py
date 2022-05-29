## Data and Dbs ##
# Modern apps create a lot of data
# In simple words, data is some raw information that has been 
#   collected or created and it can be of any tyoe such as 
#   numeric, words, digital, etc
# Thats why we store info in a DB so it can be accessed at anytime
# A DB is a systematic collection of data orin simple words, its 
#   an organized collection of data
# SQL and MySQL
# One of the most common types of DB = relational
# relational stores info in the form of tables via rows, col
# 
# DB Management system(DBMS):
# Is a collection of programs that enable the users to access
#   dbs, manipulate data, report and represent data, and also
#   control access to a database
# Hence a relational db is often referred to as a Relational DBMS
#   or (RDBMS) - very popular in the industry
# To work with relational dbs we use SQL - the standard language
#   for relational databse systems
# Structured Query Language(SQL) helps in storing, manipulating,
#   and retrieving data stored in a relational databse
# Using SQL, you can query, update, and reorganize data, as well
#   as create modify the schema(structure) of a db system and 
#   control access to its data
# Some SQL Versions:
#   MySQL - using this with python (compatible w/ major languages: 
#           Java, Python, PHP, C++, etc...)
#   MS Access
#   Oracle
#   Sybase
#   Informix
#   Postgres
#   SQL Server
#   etc ...
# 
# Basic Terminology When Working With RDBMS:
# - Data in an RDBMS is stored in db objects called tables
# - Tables are a collection of related data entries consisting of
#       numerous columns and row
# Field - Every table is broken up into smaller entities called fields
# Record - also called a row of data, is each individual entry that exists
#       in a table
# Column - A vertical entity in a table that contains all information 
#       associated with a specific field in a tabel
# NULL Value - in a table is a value in a field that appears to be blank,
#       which means a field with a NULL value is a field with no value
# Primary Key - helps us to uniquely identify a row in the table.
#       A key can not occur twice in a table
# Foreign Key - Acts like a link between two tables
# 
# Data types in MySQL:
# INT - is a normal-sized integer. We can specify a width of up to 11 digits
#       it requires 4 bytes for storage
# FLOAT(m,d) - you can display the length(m) and the number of decimals(d) 
#       this is not required and will default to 10,2 where 2 is the num of decimals
#       and 10 is the total num of digits(including decimals)
# BOOL - only used for true/false boolean conditions (1 - True) (0 - False)
# CHAR(size) - max size of 255 characters. here size is the num of chars to store
# VARCHAR(size) - can have max size of 255 chars. Variable Length String
# 
# Commands:
# CREATE DATABASE db_name;  -creates a new db with db_name as name
# SHOW DATABASES;   - shows all dbs
# USE db_name; - will connect to the db 
# DROP DATABASE db_name; - drops the db
# CREATE TABLE  table_name(columnName1 data_type, columnName2 data_type, ...) 
#   CREATE TABLE user(userId int PRIMARY KEY, username varchar(10), email varchar(25), userType varchar(10));
# 
# All queries can be created using  TablePlus#
# INSERT INTO `python_X`.`user` (`userId`, `username`, `email`, `userType`) VALUES (1528, 'Mere', 'Mere@aol.com', 'admin');