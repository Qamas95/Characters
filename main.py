from tkinter import *
import sqlite3
from tkinter import messagebox


root = Tk()
root.title("Character Databse")
root.geometry("800x800")



def addCharacter():

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()
    #Create table
    cursor.execute("""CREATE TABLE IF NOT EXISTS characters (
                        name text
                        )""") #add in future, world, lvl
    #Insert into table
    cursor.execute("INSERT INTO characters VALUES (:name)",
                {
                    'name': entryName.get()
                }
    )
    dbConnection.commit()
    dbConnection.close()

#print data from databse
def print():
    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()

    cursor.execute("SELECT *, oid FROM characters")
    
    records = cursor.fetchall()

    #loop thru results
    print_records = ''

    for record in records:
        print_records += str(record) + " " "\n"
    
    #create label to for printed records
    printLabel = Label(root, text=print_records)
    printLabel.grid(row=5, column =0, columnspan=2)

    dbConnection.commit()
    dbConnection.close()
    
def deleteChar():


    if deleteEntry.get() == '':
        return messagebox.showerror('Warning','Empty delet ID')

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()

    deleteId = deleteEntry.get()

    cursor.execute("DELETE from characters WHERE oid = " + deleteId)
    
    dbConnection.commit()
    dbConnection.close()

def switcher():
    searcher = Toplevel()
    searcher.title("Search in TCom")
    searcher.geometry("400x400")

    testLbl = Label(searcher, text="test")
    testLbl.grid(row=0, column =0)


entryName = Entry(root)
entryName.grid(row=0, column=1)

characterName = Label(root, text="Print character name")
characterName.grid(row=0, column=0)


submitButton = Button(root, text="Add Character",command=addCharacter)
submitButton.grid(row=1, column=0, columnspan=2)   

printData = Button(root, text = "Print data", command=print)
printData.grid(row=2, column=0, columnspan=2)


deleteCharacter = Button(root, text="Delete character", command = deleteChar)
deleteCharacter.grid(row=3, column =0)

deleteEntry = Entry(root)
deleteEntry.grid(row=3, column = 1)

updateCharsButton = Button(root, text="Update Characters", command=switcher)
updateCharsButton.grid(row=4, column=0, columnspan = 2)

root.mainloop()