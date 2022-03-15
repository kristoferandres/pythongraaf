# ülesanne 4
# 03.14.2022
# Kristofer Andres

from tkinter import *
import math
import time

aken = Tk()
aken.title('kalkulaator')
aken.geometry("200x200+200+500")
addlist = []
vahesumma=0
def num0():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "0")
def num1():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "1")
def num2():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "2")
def num3():
    if len(t.cget("text"))!=11:
       t.config(text = t.cget("text") + "3")
def num4():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "4")
def num5():
    if len(t.cget("text"))!=11:
       t.config(text = t.cget("text") + "5")
def num6():
    if len(t.cget("text"))!=11:
       t.config(text = t.cget("text") + "6")
def num7():
    if len(t.cget("text"))!=11:
       t.config(text = t.cget("text") + "7")
def num8():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "8")
def num9():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + "9")
def coma():
    if len(t.cget("text"))!=11:
        t.config(text = t.cget("text") + ".")
def add():
    if t.cget("text") != '='+ str(vahesumma):
        addlist.append(t.cget("text"))
    addlist.append('+')
    t.config(text='')
def minus():
    if t.cget("text") != '='+ str(vahesumma):
        addlist.append(t.cget("text"))
    addlist.append('-')
    t.config(text='')
def divide():
    if t.cget("text") != '='+ str(vahesumma):
        addlist.append(t.cget("text"))
    addlist.append('/')
    t.config(text='')
def times():
    if t.cget("text") != '='+ str(vahesumma):
        addlist.append(t.cget("text"))
    addlist.append('*')
    t.config(text='')
def equal():
    global vahesumma
    pikkus = len(addlist)/2
    pikkus = math.ceil(pikkus)
    addlist.append(t.cget("text"))
    vahesumma=float(addlist[0])
    for i in range(pikkus):
        mark = addlist[i*2+1]
        if mark== '+':
            vahesumma = vahesumma + float(addlist[i*2+2])
        if mark== '-':
            vahesumma = vahesumma - float(addlist[i*2+2])
        if mark== '/':
            vahesumma = vahesumma / float(addlist[i*2+2])
        if mark== '*':
            vahesumma = vahesumma * float(addlist[i*2+2])
    t.config(text='='+ str(vahesumma))
    
















t = Label(aken, text='', font="Tahoma 12")
t.grid(row=1, column=0, padx= 2, pady= 2, columnspan=4)
num7 = Button(aken, text="7", font="Tahoma 12", command=num7)
num7.grid(row=2, column=1, padx= 2, pady= 2)
num4 = Button(aken, text="4", font="Tahoma 12", command=num4)
num4.grid(row=3, column=1, padx= 2, pady= 2)
num1 = Button(aken, text="1", font="Tahoma 12", command=num1)
num1.grid(row=4, column=1, padx= 2, pady= 2)
num0 = Button(aken, text="0", font="Tahoma 12", command=num0)
num0.grid(row=5, column=1, padx= 2, pady= 2)
num8 = Button(aken, text="8", font="Tahoma 12", command=num8)
num8.grid(row=2, column=2, padx= 2, pady= 2)
num5 = Button(aken, text="5", font="Tahoma 12", command=num5)
num5.grid(row=3, column=2, padx= 2, pady= 2)
num2 = Button(aken, text="2", font="Tahoma 12", command=num2)
num2.grid(row=4, column=2, padx= 2, pady= 2)
coma = Button(aken, text=",", font="Tahoma 12", command=coma)
coma.grid(row=5, column=2, padx= 2, pady= 2)
num9 = Button(aken, text="9", font="Tahoma 12", command=num9)
num9.grid(row=2, column=3, padx= 2, pady= 2)
num6 = Button(aken, text="6", font="Tahoma 12", command=num6)
num6.grid(row=3, column=3, padx= 2, pady= 2)
num3 = Button(aken, text="3", font="Tahoma 12", command=num3)
num3.grid(row=4, column=3, padx= 2, pady= 2) 
equal = Button(aken, text="=", font="Tahoma 12", command=equal)
equal.grid(row=5, column=3, padx= 2, pady= 2)
divide = Button(aken, text="/", font="Tahoma 12", command=divide)
divide.grid(row=2, column=4, padx= 2, pady= 2)
times = Button(aken, text="*", font="Tahoma 12", command=times)
times.grid(row=3, column=4, padx= 2, pady= 2)
minus = Button(aken, text="-", font="Tahoma 12", command=minus)
minus.grid(row=4, column=4, padx= 2, pady= 2)
add = Button(aken, text="+", font="Tahoma 12", command=add)
add.grid(row=5, column=4, padx= 2, pady= 2)










aken.mainloop()