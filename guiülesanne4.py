# ülesanne 4
# 03.14.2022
# Kristofer Andres

from tkinter import *

aken = Tk()
aken.title('kalkulaator')
aken.geometry("200x200+200+500")

cs = 4
v = cs

text = Label(aken, text='tech', font="Tahoma 12", justify=CENTER).grid(row=1, column=0, padx= 2, pady= 2, columnspan=cs*4, sticky=E+W)
r = v * 1
num7 = Button(aken, text="7", font="Tahoma 12").grid(row=2, column=1, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 1
num4 = Button(aken, text="4", font="Tahoma 12").grid(row=3, column=1, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 1
num1 = Button(aken, text="1", font="Tahoma 12").grid(row=4, column=1, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 1
num0 = Button(aken, text="0", font="Tahoma 12").grid(row=5, column=1, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 2
num8 = Button(aken, text="8", font="Tahoma 12").grid(row=2, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 2
num5 = Button(aken, text="5", font="Tahoma 12").grid(row=3, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 2
num2 = Button(aken, text="2", font="Tahoma 12").grid(row=4, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 2
coma = Button(aken, text=",", font="Tahoma 12").grid(row=5, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 3
num9 = Button(aken, text="9", font="Tahoma 12").grid(row=2, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 3
num6 = Button(aken, text="6", font="Tahoma 12").grid(row=3, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 3
num3 = Button(aken, text="3", font="Tahoma 12").grid(row=4, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W) 
r = v * 3
equal = Button(aken, text="=", font="Tahoma 12").grid(row=5, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 4
divide = Button(aken, text="/", font="Tahoma 12").grid(row=2, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 4
times = Button(aken, text="*", font="Tahoma 12").grid(row=3, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 4
minus = Button(aken, text="-", font="Tahoma 12").grid(row=4, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)
r = v * 4
add = Button(aken, text="+", font="Tahoma 12").grid(row=5, column=r, padx= 2, pady= 2, columnspan=cs, sticky=E+W)










aken.mainloop()