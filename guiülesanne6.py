# ülesanne 6
# 03.15.2022
# Kristofer andres

from tkinter import *

aken1 = Tk()
aken1.title('Lipp')



c = Canvas(aken1, width=300, height=400)
c.pack()

c.create_rectangle(0,100,300,200, fill="#be0026", outline= '#be0026')
c.create_oval(56,43,178,165, fill="white", outline= 'white')
c.create_rectangle(0,0,300,100, fill="white", outline= 'white')
c.create_arc(56, 42, 178, 164, extent=180, fill="#be0026", outline= '#be0026')

minu_pilt = PhotoImage(file='greenland.gif')
c.create_image(0, 200, anchor=NW, image=minu_pilt)

aken1.mainloop()
