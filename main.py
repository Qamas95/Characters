from tkinter import *

root = Tk()
root.title("Character Databse")
root.geometry("600x150")

def addCharacter():
    return


characterName = Label(root, text="Print character name")
characterName.grid(row=0, column=0)
entryName = Entry(root)
entryName.grid(row=0, column=1)

submitButton = Button(root, text="Add Character",command=addCharacter)
submitButton.grid(row=1, column=0, columnspan=2)

root.mainloop()