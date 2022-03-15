# ülesanne 5
# 03.15.2022
# Kristofer Andres

from tkinter import *

aken = Tk()
aken.title('käibemaksukalkulaator')

def arvuta():
    if var.get()==1:
        arv = int(s.get()) * 0.1
        arv = round(arv, 2)
        t1.config(text=str(arv)+"€")
        arv = int(s.get()) * 1.1
        arv = round(arv, 2)
        t2.config(text=str(arv)+"€")
    if var.get()==2:
        arv = int(s.get()) * 0.2
        arv = round(arv, 2)
        t1.config(text=str(arv)+"€")
        arv = int(s.get()) * 1.2
        arv = round(arv, 2)
        t2.config(text=str(arv)+"€")
        



t = Label(aken, text="hind käibemaksuta:")
t.grid(row = 0,column = 0)

t = Label(aken, text="käibemaksumäär")
t.grid(row = 1,column = 0, rowspan = 2, sticky = S+N)

t = Label(aken, text="käibemaks")
t.grid(row = 3,column = 0)

t = Label(aken, text="hind käibemaksuga")
t.grid(row = 4,column = 0)


s = Entry(aken)
s.grid(row = 0,column = 1)

var = IntVar()
valikukast = Radiobutton(aken,text="10%", variable=var, value=1)
valikukast.grid(row = 1, column = 1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=2)
valikukast.grid(row = 2, column = 1)

t1 = Label(aken, text="0.00€")
t1.grid(row = 3,column = 1)

t2 = Label(aken, text="0.00€")
t2.grid(row = 4,column = 1)

nupp = Button(aken, text="OK", command = arvuta)
nupp.grid(row=5, column=1, ipadx= 15)




aken.mainloop()