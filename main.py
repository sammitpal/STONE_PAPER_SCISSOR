from tkinter import *
from random import randint
root = Tk()
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)
root.title("STONE PAPER SCISSOR")
head = Label(root,text="STONE PAPER SCISSOR")
head.grid(row=0,column=3)

user = Label(root,text="User")
computer = Label(root,text="Computer")
user.grid(row=3,column=2)
computer.grid(row=3,column=4)

options = ["Stone","Paper","Scissor"]
uservalue = StringVar()
uservalue.set(options[0])

def play(event):
    global u
    global c
    value = randint(0, 5)
    if value == 0 or value == 1:
        str = "Stone"
    elif value == 2 or value == 3:
        str = "Paper"
    else:
        str = "Scisscor"
    output = Label(root, text=str)
    output.grid(row=5, column=4)

drop = OptionMenu(root,uservalue,*options,command=play)
drop.grid(row=5,column=2,padx=10)


root.mainloop()