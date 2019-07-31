import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox

fileName="movieList.txt"
listOfMovies=[]

class Movie:
    def __init__(self,name,category,description,price):
        self.__name=name
        self.__category=category
        self.__description=description
        self.__price=price
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getCategory(self):
        return self.__category
    def setCategory(self,category):
        self.__category=category
    def getDescription(self):
        return self.__description
    def setDescription(self,description):
        self.__description=description
    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        self.__price=price
    def getPriceWithGST(self):
        return(round(self.__price*1.07,2))

#-->Assignment to change this to load from database
#load data from some supplied filename
def loadData(fileName):
	#Load Data to GUI
	file=open(fileName,'r')
	lines=file.readlines()
	movieLists=[]

	for eachLine in lines:
		eachLine=eachLine.replace("\n","")
		cols=eachLine.split("|")
		name=cols[0]
		category=cols[1]
		description=cols[2]
		price=float(cols[3])
		movieList=Movie(name,category,description,price)
		movieLists.append(movieList)
	
	file.close()


	return movieLists

#update Tree View of travel package info
def updateTreeView():
	#clear all items in the tree view
	for i in tree1.get_children():
		tree1.delete(i)
	i=0

	for movie in listOfMovies:
		#bind the iid with the List item index
		tree1.insert("",i,text=movie.getName(),iid=str(i))
		i+=1

	clearTextBoxes()

def reloadData():
	global listOfMovies
	listOfMovies=loadData(fileName)
	updateTreeView()
	messagebox.showinfo("Data Load","Data Loaded!")


#search and filter matching movie
def filtermovie():
	
	#clear treeview items
	for i in tree1.get_children():
		tree1.delete(i)

	i=0
	searchStr=txtNameFilter.get().upper()
	#print(searchStr)

	for movie in listOfMovies:
		#match substring 
		if movie.getName().upper().find(searchStr)>-1:
			#bind the iid with the List item index
			tree1.insert("",i,text=movie.getName(),iid=str(i))
		
		i+=1
		
	clearTextBoxes()

def clearTextBoxes():
    #clear text in textboxes
    txtCategory.set("")
    #txtDescription.set("")
    txtPrice.set("")
    textDescription.config(state=tk.NORMAL)
    textDescription.delete(1.0, tk.END)
    textDescription.config(state=tk.DISABLED)
def selectItem(e):
    curItem = tree1.selection()
    print(curItem[0]) #get the iid 
    iid=int(curItem[0])
    print(listOfMovies[iid].getName())

    txtCategory.set(listOfMovies[iid].getCategory())
    #txtDescription.set(listOfMovies[iid].getDescription())
    txtPrice.set("$"+str(listOfMovies[iid].getPriceWithGST()))
    
    textDescription.config(state=tk.NORMAL)
    textDescription.delete(1.0, tk.END)
    textDescription.insert(tk.END,listOfMovies[iid].getDescription())
    textDescription.config(state=tk.DISABLED)

#Main GUI	
window = tk.Tk() 
window.title("SP Movie")
window.geometry("350x600") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction

labelAppName=ttk.Label(window,text="SP Movie App",padding=2)
labelAppName.config(font=("Courier", 20))
labelAppName.grid(row=0,column=1,columnspan=3,pady=10)

txtNameFilter=StringVar()
entry1=ttk.Entry(window,textvariable=txtNameFilter)
entry1.grid(row=1,column=1)
buttonSearch=ttk.Button(window,text='Filter Movie',command=filtermovie)
buttonSearch.grid(row=1,column=2)

#treeview
tree1=ttk.Treeview(window)
tree1.heading("#0",text="Movie Name")

tree1.grid(row=2,column=1,columnspan=2,pady=15)
tree1.bind('<ButtonRelease-1>', selectItem)

#movie Item Details
labelCategory=ttk.Label(window,text="Category",padding=2)
labelCategory.grid(row=3,column=0,sticky=tk.W)
txtCategory=StringVar()
textCategory=ttk.Entry(window,textvariable=txtCategory,state='readonly')
textCategory.grid(row=3,column=1,pady=2)


labelDescription=ttk.Label(window,text="Description",padding=2)
labelDescription.grid(row=4,column=0,sticky=tk.W)
#Entry is single line text box
#txtDescription=StringVar()
#textDescription=ttk.Entry(window,textvariable=txtDescription,state='readonly',width=34)
#textDescription.grid(row=4,column=1,columnspan=2,pady=2)
textDescription=tk.Text(height=10,width=25,wrap=tk.WORD)
textDescription.grid(row=4,column=1,columnspan=2,pady=4)
textDescription.config(state=tk.DISABLED)

labelPrice=ttk.Label(window,text="Price(GST)",padding=2)
labelPrice.grid(row=5,column=0,sticky=tk.W)
txtPrice=StringVar()
textPrice=ttk.Entry(window,textvariable=txtPrice,state='readonly')
textPrice.grid(row=5,column=1,pady=2)

button1=ttk.Button(window,text='Reload Data',command=reloadData)
button1.grid(row=6,column=0,columnspan=3,pady=10)

#load text file data and get the list Of movie
listOfMovies=loadData(fileName)
updateTreeView()

window.mainloop() #main loop to wait for events
