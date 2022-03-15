# ülesanne 3
# 03.14.2022
# Kristofer Andres

from tkinter import *

aken = Tk()
aken.title('Kristofer Andres')
aken.configure(background='black')
aken.iconbitmap('gems.ico')
aken.resizable(0, 0)


tekst = Label(aken, text="Nimi: Kristofer Andres", fg='red', bg='black', pady=0, padx=30, font="Tahoma 16 bold italic")
tekst.pack()

tekst = Label(aken, text="Rühm: IT21", fg='red', bg='black', pady=0, padx=30, font="Tahoma 16 bold italic")
tekst.pack()

tekst = Label(aken, text="2022", fg='red', bg='black', pady=0, padx=30, font="Tahoma 16 bold italic")
tekst.pack()


aken.mainloop()