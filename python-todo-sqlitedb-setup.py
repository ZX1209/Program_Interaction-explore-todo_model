import sqlite3

# db-sqlite3-todo
# 

connect = sqlite3.connect('db-sqlite3-todo')
cursor = connect.cursor()


cursor.execute()
# ID INTEGER PRIMARY KEY NOT NULL
# todos(id int  primary key not null,title text,state text)

connect.commit()
connect.close()