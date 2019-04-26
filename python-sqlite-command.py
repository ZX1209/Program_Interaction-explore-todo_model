import sqlite3
import fire

# db-sqlite3-todo
# 

def todo(s):
    connect = sqlite3.connect('db-sqlite3-todo')
    cursor = connect.cursor()


    cursor.execute("insert into todos(title,state) values(?,?)",(s,"todo"))
    # ID INTEGER PRIMARY KEY NOT NULL
    # todos(id int  primary key not null,title text,state text)


    connect.commit()
    connect.close()

def done(s):
    connect = sqlite3.connect('db-sqlite3-todo')
    cursor = connect.cursor()


    cursor.execute("update todos set state='done' where title=?",(s,))
    # ID INTEGER PRIMARY KEY NOT NULL
    # todos(id int  primary key not null,title text,state text)


    connect.commit()
    connect.close()

def show():
    connect = sqlite3.connect('db-sqlite3-todo')
    cursor = connect.cursor()


    cursor.execute("select * from todos")
    # ID INTEGER PRIMARY KEY NOT NULL
    # todos(id int  primary key not null,title text,state text)
    tmp = cursor.fetchall()

    connect.commit()
    connect.close()
    return tmp


def show_col():
    connect = sqlite3.connect('db-sqlite3-todo')
    cursor = connect.cursor()


    cursor.execute("PRAGMA table_info(todos)")
    # ID INTEGER PRIMARY KEY NOT NULL
    # todos(id int  primary key not null,title text,state text)
    tmp = cursor.fetchall()

    connect.commit()
    connect.close()
    return tmp
if __name__ == '__main__':
    fire.Fire()