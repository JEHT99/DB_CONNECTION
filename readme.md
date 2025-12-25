# Requirements
This library has been tested on **Python 3.13.5**.

## To run Sqlite
```cmd
> pip install python-dotenv==1.1.1
```

## To run Postgres
```cmd
> pip install python-dotenv==1.1.1
> pip install psycopg2==2.9.10
```
## How to import them
Drop **absDb.py** & **postgreSql.py** or **sqLite.py** into your project, now just call them:
```python
from postgreSql import PostgreSQL
from sqLite import SQLite
```
**Note:** The **.env** shows a template of the envirioment variables, just adjust every parameter to the ones you will use.

# How to use a class
You only have to be noticed about your database structure to do queries, here is an example:
```python
from dbConecction import PostgreSQL
#------------------------------------------------------------
db = PostgreSQL()
sql = "INSERT INTO tb_users (nickname) VALUES ('JEHT99');"
print(db.setData(sql))

sql = "SELECT * FROM tb_users;"
print(db.getdata(sql))

sql = "DELETE FROM tb_users RETURNING nickname;"
print(db.setDataReturning(sql))
```
The first query will returns True, the second one will prints a list of all users in the table, finally the third query will returns a list with the nickname attribute of all the deleted records.

# How the classes works
There are three methods to interact to the database manager:
```python
def getdata(self, sql:str, values:tuple=())-> list
#------------------------------------------------------------
def setData(self, sql:str, values:tuple=())-> bool
#------------------------------------------------------------
def setDataReturning(self, sql:str, values:tuple=())-> list
#------------------------------------------------------------
```

1. **getdata:** Works with **SELECT** queries.
1. **setData:** Works with **INSERT**, **UPDATE** & **DELETE** queries.
1. **setDataReturning:** Works exactly as the previous one but with the diference it returns desired data.

**Note:** Each method receives two parameters, a sql instruction and a tuple of values that are use for avoid sql injection, the second one is optional. Also if something went wrong during the query process any changes are restored to the state before executed the sql instruction.