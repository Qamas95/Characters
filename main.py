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

root.mainloop()