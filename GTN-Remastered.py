from tkinter.ttk import *
from ttkthemes import ThemedTk
from tkinter import *
import random
tries = 0

win = ThemedTk(theme = "kroc")
win.configure(themebg="kroc")


def Byebye():
    win.destroy()



def randomize():
    global tries
    global numbers
    global a
    tries = 0
    T.config(text="Tries:  " + str(tries))
    Dicelbl.configure(image = Dice)
    if choice.get() == 1:
        a = 50
    elif choice.get() == 2:
        a = 100
    elif choice.get() == 3:
        a = 500
    numbers = random.randint(0, a)
    print(numbers)

def game(*args):
    global numbers
    global tries
    global a
    if int(entry.get()) == numbers:
        Dicelbl.configure(image= correct)
        T.config(text="Tries:  " + str(tries),)
        entry.delete(0, END)
    elif int(entry.get()) < numbers:
        Dicelbl.configure(image=up)
        tries += 1
        T.config(text="Tries:  " + str(tries))
        entry.delete(0, END)
    elif int(entry.get()) > numbers:
        Dicelbl.configure(image=down)
        tries += 1
        T.config(text="Tries:  " + str(tries))
        entry.delete(0, END)

    if tries <= 5:
        T.config(text="Tries:  " + str(tries), fg='green')
    elif tries <= 10:
        T.config(text="Tries:  " + str(tries), fg='yellow')
    elif tries >= 11:
        T.config(text="Tries:  " + str(tries), fg='red')
    #if int(entry.get()) > int(choice.get()):
        #Dicelbl.configure(text = "YOU ARE KIDDING ME")Unrealeased things


    #mia tripli IF pou tha tsekarw ti sexsh exei to entry me to numbers kai tha emfanizei tin swsth eikona
    #tha efxanei ta tries kata 1
choice = IntVar()
choice.set(2)
Dice = PhotoImage(file="Image20240402201808.png")
correct = PhotoImage(file="Image20240402201832.png")
up = PhotoImage(file="Image20240402201836.png")
down = PhotoImage(file="Image20240402201838.png")

Tlbl = Label(win , text = "Guess the number",borderwidth=7,font=('Tahoma', 22),bg="lightblue")
exclbl = Label(win, text="In this game you have to find the number ""\n that is randomly chosen every round.\nTry to guess it with the least possible tries!",font=('tahoma',16))
c1 = Radiobutton(win, text ="Easy",value=1,variable=choice)
c2 = Radiobutton(win, text ="Normal",value=2,variable=choice)
c3 = Radiobutton(win, text ="Hard ",value=3,variable=choice )
entry = Entry(win,font=('Tahoma',10),width=22, )
ranbtn = Button(win,text="Randomize",width=10,font=('Tahoma',10),height=3,command=randomize)
checkbtn= Button(win,text="Exit",width=10,font=('Tahoma',10),height=3,command=Byebye)
T= Label(win , text = "Tries:    ",font=('Tahoma', 12),bg="lightblue")
Dicelbl = Label(win,text="",image=Dice,bg="lightblue")





#place
Tlbl.pack()
c2.pack()
exclbl.pack()
c1.place(x=100,y=51)
c3.place(x=250,y=51)
entry.pack()
ranbtn.place(x=320,y=175)
checkbtn.place(x=320,y=230)
T.place(x=120,y=177)
Dicelbl.place(x=0,y=200)


win.title("My first tkinter window") # TITLOS PARATHYROU
win.geometry('400x400') # MEGETHOS PARATHYROU




win.bind('<Return>',game)
win.mainloop()