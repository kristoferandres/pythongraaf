#ülesanne 2
#03.14.2022
#Kristofer Andres

import turtle

aken = turtle.Screen()
aken.setup(700, 300)
aken.title('Ülesanne 2 Kristofer Andres')



t= turtle.Turtle()
t.penup()
t.forward(200)
t.pendown()
for i in range(5):
    t.forward(100)
    t.right(144)
    
def kolmnurk(pikkus, varv):
    t= turtle.Turtle()
    for i in range(3):
        t.color(varv)
        t.forward(pikkus)
        t.left(120)
        

p= int(input('sisesta kolmnurga pikkus: '))
c= input('sisesta kolmnurga värv: ')
kolmnurk(p, c)
turtle.exitonclick