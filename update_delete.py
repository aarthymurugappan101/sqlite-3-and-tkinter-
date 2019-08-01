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
        messagebox.showinfo("information","Database Initialized")
        conn.commit()

    conn.close()
#print(os.path.join(os.getcwd(), 'moviedata.db'))

def deleteMovie():
    name = movie_name.get()
    conn = sqlite3.connect('moviedata.db')
    sql = "Delete from movies WHERE name=?"
    conn.execute(sql,(name,))
    messagebox.showinfo("information","MOVIE DELETED")
    conn.commit()
    conn.close()

def insertMovie():
    conn = sqlite3.connect('moviedata.db')
    entry_name = nameent.get()
    entry_category = catent.get()
    entry_descrition = descent.get()
    entry_price = priceent.get()
    sql = "INSERT OR REPLACE INTO movies(name,category,description,price)VALUES(?,?,?,?)"
    conn.row_factory = sqlite3.Row
    args = (entry_name,entry_category,entry_descrition,entry_price)
    conn.execute(sql,args)
    messagebox.showinfo("information","Movie Inserted")
    conn.commit()
    conn.close()

if not os.path.exists('moviedata.db'):
    initDataBase()

# main gui
window = tk.Tk()
window.title("SP Movie Admin Form")
window.geometry("400x250")
window.resizable(0, 0)

labelAppName=ttk.Label(window,text="SP Movie Admin Page",padding=2)
labelAppName.config(font=("Courier", 20))
labelAppName.grid(row=0,column=1,columnspan=3,pady=10)

lName = ttk.Label(window,text="Name",padding=2)
lName.grid(row=1,column=1,columnspan=1)
movie_name = StringVar()
nameent = ttk.Entry(window,textvariable=movie_name)
nameent.grid(row=1,column=2,columnspan=3)

lcat = ttk.Label(window,text="Category",padding=2)
lcat.grid(row=2,column=1,columnspan=1)
movie_cat = StringVar()
catent = ttk.Entry(window,textvariable=movie_cat)
catent.grid(row=2,column=2,columnspan=3)

ldesc = ttk.Label(window,text="description",padding=2)
ldesc.grid(row=3,column=1,columnspan=1)
moviedesc = StringVar()
descent = ttk.Entry(window,textvariable=moviedesc)
descent.grid(row=3,column=2,columnspan=3)

lprice = ttk.Label(window,text="Price",padding=2)
lprice.grid(row=4,column=1,columnspan=1)
movie_price = StringVar()
priceent = ttk.Entry(window,textvariable=movie_price)
priceent.grid(row=4,column=2,columnspan=3)

buttoninsert = ttk.Button(window,text="Insert",command=insertMovie)
buttoninsert.grid(row=7,column=1)

buttondelete = ttk.Button(window,text="Delete",command=deleteMovie)
buttondelete.grid(row=7,column=2)

window.mainloop()