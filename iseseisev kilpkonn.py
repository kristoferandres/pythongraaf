#iseseisev kilpkonn
#14.03.2022
#Kristofer Andres

import turtle
aken= turtle.Screen()
aken.setup(300, 300)
aken.title('laheasi')


#kui tahad näha esimest pane see 0 ks kui teist pane see üheks
esimene=1

k1 = turtle.Turtle()
k1.speed(5)
p= 90
e= 40
k= 1
if esimene==1:
    p= -90
    e= -40
    k=4



for b in range(k):
    for i in range(4):
        for a in range(2):
            k1.forward(e)
            k1.right(p)
            k1.forward(e)
            k1.left(p)
        k1.right(p)
        k1.backward(e)
    k1.right(p)
    
turtle.exitonclick