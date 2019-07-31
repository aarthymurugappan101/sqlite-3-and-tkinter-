import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
import sqlite3 
import os.path 

def initDataBase():
    conn=sqlite3.connect('moviedata.db')
    sql ="create table movies(name Text primary key, category Text, description Text, price Real)"
    conn.execute(sql)
    conn.commit()

    file = open('C:\\Users\\gayat\\Desktop\\web dev\\assign2\\2761812.txt')
    lines = file.readlines()

    for data in lines:
        data = data.replace('\n','')
        cols = data.split('|')
        name = cols[0]
        category = cols[1]
        description = cols[2]
        price = float(cols[3])

        sql = "Insert Into movies(name,category,description,price)values(?,?,?,?)"
        args=(name,category,description,price)
        conn.execute(sql,args)
        conn.commit()

    conn.close()
#print(os.path.join(os.getcwd(), 'moviedata.db'))

def deleteStudent(name):
    conn = sqlite3.connect('moviedata.db')
    sql = "Delete from movies WHERE name=?"
    conn.execute(sql,(name,))
    conn.commit()
    conn.close()

def insertMovie():
    conn = sqlite3.connect('moviedata.db')
    entry_name = nameent
    entry_category = catent
    entry_descrition = descent
    entry_price = priceent
    sql = "INSERT OR REPLACE INTO movies(name,category,description,price)VALUES(?,?,?,?)"
    conn.row_factory = sqlite3.Row
    args = (entry_name,entry_category,entry_descrition,entry_price)
    conn.execute(sql,args)
    conn.commit()
    conn.close()

if not os.path.exists('moviedata.db'):
    initDataBase()

# main gui
