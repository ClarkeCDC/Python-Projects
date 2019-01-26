#set imports
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
#set window
window = Tk()
window.title("welcome noobs")
window.geometry("700x550")
#set menu
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="New")
new_item.add_command(label="Edit")
menu.add_cascade(label="File", menu=new_item)
window.config(menu=menu)
#create functions
def buttonClicked():
    res = textField.get()
    label.configure(text=res)
def radioButtonClicked():
    print(selected.get())
def messageButtonClicked():
    messagebox.showinfo("Title", "Content")
    #messagebox.showerror
    #messagebox.showwarning
# res = messagebox.askquestion('Message title','Message content')
# res = messagebox.askyesno('Message title','Message content')
# res = messagebox.askyesnocancel('Message title','Message content')
# res = messagebox.askokcancel('Message title','Message content')
# res = messagebox.askretrycancel('Message title','Message content')
# Theese return true of yes and false if no
#set labels
label = Label(window, text="hello world", font=("krungthep", 18))
label.grid(column=0, row=0)
#set text fields
textField = Entry(window, width=10)
textField.grid(column=0, row=1)
#set combobox
combo = Combobox(window)
combo["values"] = [1,2,3,4,5, "Text"]
combo.current(1)
combo.grid(column=1, row=1)
#set checkboxes
check_state = BooleanVar()
check_state.set(1)
check = Checkbutton(window, text="check", var=check_state)
check.grid(column=2, row=1)
#set radioButtons
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

rad1.grid(column=0, row=3)
rad2.grid(column=0, row=4)
rad3.grid(column=0, row=5)
#set scrolledtexxt
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=7)
txt.insert(INSERT, "Text goes here lol")
#set spinBox number box
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=8)
#set progressbar
style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="black")
bar = Progressbar(window, length= 200, style="black.Horizontal.TProgressbar")
bar.grid(column=0, row=9)
bar["value"] = 70
#set filedialog
filed = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

#set buttons
button = Button(window, text="Click ME!", command=buttonClicked)
button.grid(column=0, row=2)
button2 = Button(window, text="Click ME!", command=radioButtonClicked)
button2.grid(column=0, row=6)
msgButton = Button(window, text="Message Box", command=messageButtonClicked)
msgButton.grid(column=1, row=6)
window.mainloop()