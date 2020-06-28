from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import filedialog

import requests
import json
import pandas as pd
import os



root = Tk()
root.title("Character Databse")
root.geometry("800x800")

global character_numbers



def clearDatabase():
    result = messagebox.askyesno('Question', 'Do you wanna delete all character from databse?')
    if result == True:
        #Create db and connect
        dbConnection = sqlite3.connect('characters.db')
        #Create cursor
        cursor = dbConnection.cursor()
        cursor.execute("DELETE FROM characters;")
        messagebox.showinfo('Info','You have deleted ' + str(cursor.rowcount) + ' characters')
        dbConnection.commit()
        dbConnection.close()
        #Create db and connect
        dbConnection = sqlite3.connect('characters.db')
        #Create cursor
        cursor = dbConnection.cursor()
        cursor.execute("DELETE FROM characters;")
        dbConnection.commit()
        dbConnection.close()
    elif result == False:
        return messagebox.showinfo('Info','You have not deleted any characters')
    

def addCharacter():

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()
    #Create table
    cursor.execute("""CREATE TABLE IF NOT EXISTS characters (
                        name text
                        )""")
    #Insert into table
    cursor.execute("INSERT INTO characters VALUES (:name)",
                {
                    'name': entryName.get()
                }
    )

    entryName.delete(0,END)
    dbConnection.commit()
    dbConnection.close()

def deleteChar():

    if deleteEntry.get() == "":
        return messagebox.showerror('Warning','Enter character name you want to delete')
        
    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()

    deleteName = deleteEntry.get()


    cursor.execute("DELETE FROM characters WHERE name=?",(deleteName,))
    
    deleteEntry.delete(0,END)
    dbConnection.commit()
    dbConnection.close()

def switcher():


    searcher = Toplevel()
    searcher.title("Search in TCom")
    searcher.geometry("400x400")

    scrollbar = Scrollbar(searcher)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(searcher)
    listbox.pack(fill=BOTH, expand=1)

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()
    
    cursor.execute("SELECT name FROM characters")
    names = cursor.fetchall()

    print_names = []
    character_numbers = 0
    for item in names:
        print_names += item
        character_numbers += 1

    api_data = dict()

    labels = []
    del labels[:]
    for i in range(character_numbers):
            api_request = requests.get("https://api.tibiadata.com/v2/characters/"+print_names[i]+".json")
            data = json.loads(api_request.text)
            api_data.update({i: data})
            name = api_data[i]['characters']['data']['name']
            vocation = api_data[i]['characters']['data']['vocation']
            level = api_data[i]['characters']['data']['level']
            residence = api_data[i]['characters']['data']['residence']
            world = api_data[i]['characters']['data']['world']
            z = i+1
            listbox.insert(END,str(z) + " - " + name + " | " + vocation + " | " + "Lvl: " + str(level) + " | " + residence + " | " + world)

            #previous print, now data list available in scroll box
            # labels.append(Label(searcher,text=str(z) + " - " + name + " | " + vocation + " | " + "Lvl: " + str(level) + " | " + residence + " | " + world))
            # labels[i].place(x=10,y=10+(30*i))


    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    dbConnection.commit()
    dbConnection.close()

def savexlsx():

    #Create db and connect
    dbConnection = sqlite3.connect('characters.db')
    #Create cursor
    cursor = dbConnection.cursor()

    cursor.execute("SELECT name FROM characters")
    names = cursor.fetchall()

    print_names = []
    character_numbers = 0
    for item in names:
        print_names += item
        character_numbers += 1

    api_data = dict()
    d = []

    for i in range(character_numbers):
            api_request = requests.get("https://api.tibiadata.com/v2/characters/"+print_names[i]+".json")
            data = json.loads(api_request.text)
            api_data.update({i: data})
            name = api_data[i]['characters']['data']['name']
            vocation = api_data[i]['characters']['data']['vocation']
            level = api_data[i]['characters']['data']['level']
            residence = api_data[i]['characters']['data']['residence']
            world = api_data[i]['characters']['data']['world']
            d.append((name,vocation,level,residence,world))
            
    df = pd.DataFrame(d,columns=('Name','Vocation','Level','Residence','World'))
    df.index += 1


    df.to_excel("test.xlsx",sheet_name='characters')


    dbConnection.commit()
    dbConnection.close()

def openGame():

    try:
        os.startfile('C:/Users/kk/AppData/Local/Tibia/Tibia.exe')
    except:
        print("Can't open file")




characterName = Label(root, text="Enter character name")
characterName.grid(row=0, column=0)

entryName = Entry(root)
entryName.grid(row=0, column=1)


addChar = Button(root, text="Submit",command=addCharacter)
addChar.grid(row=0, column=2, ipadx=23)   


deleteChars = Label(root, text="Delete character name")
deleteChars.grid(row=1, column=0)

deleteEntry = Entry(root)
deleteEntry.grid(row=1, column = 1)

deleteCharacter = Button(root, text="Delete character", command = deleteChar)
deleteCharacter.grid(row=1, column =2)



updateCharsButton = Button(root, text="Print characters", command=switcher)
updateCharsButton.grid(row=2, column=0, columnspan = 3, pady=10, padx=10, ipadx=150)

clearDB = Button(root, text="Clear Database", command=clearDatabase)
clearDB.grid(row=3, column=0, columnspan = 3, pady=10, padx=10, ipadx=150)


addExcel = Button(root, text="Save in Excel", command=savexlsx)
addExcel.grid(row=4, column=0, columnspan = 3, pady=10, padx=10, ipadx=155)

startGame = Button(root, text="Open Game", command=openGame)
startGame.grid(row=5, column=0, columnspan = 3, pady=10, padx=10, ipadx=155)





root.mainloop()