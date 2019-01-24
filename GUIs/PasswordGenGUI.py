from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import random
import csv
"""Set Up all functions"""
alphabet=[]
def getAsciiCharacters():
    print("Gaining all characters")
    for i in range(97,123):
        alphabet.append(chr(i))

    for i in range(65,91):
        alphabet.append(chr(i))

    for i in range(0,10):
        alphabet.append(str(i))
    alphabet.append("!")
    alphabet.append("$")
getAsciiCharacters()
def saveToCsv(account, password):
    with open("passwords.csv", "a") as csvfile:
        fieldnames = ["account", "password"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow({"account": account, "password": password})
        csvfile.close()
def printPasswords():
    TextBox.delete(1.0, END)
    with open("passwords.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            TextBox.insert(INSERT,"Account: " + row["account"] + "  Password: " + row["password"] + "\n" )
            #print("Account: " + row["account"] + "  Password: " + row["password"])
        csvFile.close()
def createPassword():
    password = []
    length = int(spinbox.get())
    for i in range(length):
        password.append(random.choice(alphabet))

    saveToCsv(TextfieldUsername.get(), "".join(password))
    printPasswords()
def deletePassword():
    if(TextFieldDelete.get() == ""):
        messagebox.showerror(title="Account Name", message="No Account name was supplied")
    else:  
        with open("passwords.csv","r") as file:
            printPasswords()
            lines = file.readlines()
            line = 0
            account = TextFieldDelete.get()
            for row in lines:
                if account in row:
                    del lines[int(line)]
                    open("passwords.csv","w").writelines(lines)
                line = line + 1
        printPasswords()

window = Tk()
window.title("Password Manager")
window.geometry("600x450")

"""Declare items"""
lblUsername = Label(window, text="Username")
lblPassword = Label(window, text="Password Length")
lblDeletePassword = Label(window, text="Delete Password For Account:")
TextFieldDelete = Entry(window, width=20)
TextfieldUsername = Entry(window, width=20)
TextBox = scrolledtext.ScrolledText(window, width=50, height=15)
spinbox = Spinbox(window, from_=4, to=25)
btnCreatePassword = Button(window, text="Create Password", command=createPassword)
btnDeletePassword = Button(window, text="Delete Password", command=deletePassword)
"""Set item points"""
##lblUsername.grid(column=0, row=0)
##TextfieldUsername.grid(column=1, row=0)
##lblPassword.grid(column=0, row=1)
##spinbox.grid(column=1, row=1)
##btnCreatePassword.grid(column=1, row=2)
##TextBox.grid(column=1, row=4)
##lblDeletePassword.grid(column=0, row=5)
##TextFieldDelete.grid(column=1, row=5)
##btnDeletePassword.grid(column=1, row=6)
lblUsername.pack()
TextfieldUsername.pack()
lblPassword.pack()
spinbox.pack()
btnCreatePassword.pack()
TextBox.pack()
lblDeletePassword.pack()
TextFieldDelete.pack()
btnDeletePassword.pack()
printPasswords()
window.mainloop()
