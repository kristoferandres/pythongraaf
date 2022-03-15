# ülesanne 1
# 03.14.2022
# Kristofer Andres

import random
import turtle

aken = turtle.Screen()
aken.setup(300, 300)
aken.title('Ülesanne 1 Kristofer Andres')

colors = ['red', 'green', 'orange', 'blue']

kord = 8192
keer = 0
k=1
turtle.exitonclick

for a in range(kord):
    t = turtle.Turtle()
    t.speed(10)
    t.color(random.choice(colors))
    if keer > 180:
        k = 0
        keer=360/kord
    if k == 0:
        t.right(keer) 
    else:
        t.left(keer)
    t.forward(100)
    keer+= 360/kord
    

    