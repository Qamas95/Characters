from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Character Databse")
root.geometry("600x150")

entryName = Entry(root)
entryName.grid(row=0, column=1)

def addCharacter():

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()
    #Create table

    
    #Todo: If table exist skip creating table!
    
    cursor.execute("""CREATE TABLE characters (
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


characterName = Label(root, text="Print character name")
characterName.grid(row=0, column=0)


submitButton = Button(root, text="Add Character",command=addCharacter)
submitButton.grid(row=1, column=0, columnspan=2)


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
    printLabel.grid(row=3, column =0, columnspan=2)

    dbConnection.commit()
    dbConnection.close()

printData = Button(root, text = "Print data", command=print)
printData.grid(row=2, column=0, columnspan=2)

root.mainloop()