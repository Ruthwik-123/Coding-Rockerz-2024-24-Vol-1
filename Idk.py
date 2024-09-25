import turtle
from turtle import *
import random
from random import randint
import time
a = turtle.Screen()
a.addshape('123.gif')
write = Turtle()
write.up()
write.goto(-100,0)
write.hideturtle()
#setup
t = Turtle()
turtle.bgcolor("navy")
turtle.setup(1000,600)
t.speed(175)
t.hideturtle()
t.penup()
t.goto(-450,250)
t.pendown()
#stars
for i in range(8):
    for i in range(27):
        t.color(random.choice(["red", "orange", "yellow", "green","white","pink","peru","cyan"]))
        t.begin_fill()
        for i in range(5):
            t.left(144)
            t.forward(15)
        t.end_fill()
        t.penup()
        t.forward(35)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(1000)
    t.left(180)
    t.pendown()
    for i in range(28):
        t.color(random.choice(["red", "orange", "yellow", "green","white","pink","peru","cyan"]))
        t.begin_fill()
        for i in range(5):
            t.left(144)
            t.forward(15)
        t.end_fill()
        t.penup()
        t.forward(35)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(925)
    t.left(180)
    t.pendown()
#players
ra = Turtle()
ra.shape('123.gif')
ra.shapesize(1)
ra.penup()
ra.goto(-420,260)
ra.pendown()
rb = Turtle()
rb.shape('123.gif')
rb.shapesize(1)
rb.penup()
rb.goto(-420,100)
rb.pendown()
rc = Turtle()
rc.shape('123.gif')
rc.shapesize(1)
rc.penup()
rc.goto(-420,-100)
rc.pendown()
rd = Turtle()
rd.shape('123.gif')
rd.shapesize(1)
rd.penup()
rd.goto(-420,-260)
rd.pendown()
ra.penup()
rb.penup()
rc.penup()
rd.penup()

t.up()
t.goto(260, 300)
t.down()
t.color('white', 'black')
for i in range(15):
    t.begin_fill()
    t.forward(40) #Increase the size here
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40) #Increase the size here
    t.right(90)
    t.forward(40)
    t.up()
    t.backward(40)
    t.right(90)
    t.down()
    t.end_fill()

time.sleep(5)




while ra.xcor() <= 200 and rb.xcor() <= 200 and rc.xcor() <= 200 and rd.xcor() <= 200:
    ra.forward(randint(1,15))
    rb.forward(randint(1,15))
    rc.forward(randint(1,15))
    rd.forward(randint(1,15))

if ra.xcor() > rb.xcor() and ra.xcor() > rc.xcor() and ra.xcor() >  rd.xcor() :
    print('Rocket A won')
    write.write('Rocket A wins',font=('arail', 32, 'bold'))
    #ra.color('black')
    for i in range(72):
        ra.right(5)
        ra.shapesize(2.5)


elif rb.xcor() > ra.xcor() and rb.xcor() > rc.xcor() and rb.xcor() >  rd.xcor() :
    print('Rocket B won')
    rb.shapesize(2.5)
    #rb.color('black')
    write.write('Rocket B won',font=('arail', 32, 'bold'))
    for i in range(72):
        rb.right(5)
        rb.shapesize(2.5)

elif rc.xcor() > ra.xcor() and rc.xcor() > rb.xcor() and rc.xcor() >  rd.xcor() :
    print('Rocket C won')
    rc.shapesize(2.5)
    #rc.color('black')
    write.write('Rocket C won',font=('arail', 32, 'bold'))
    for i in range(72):
        rc.right(5)
        rc.shapesize(2.5)

else:
    print('Rocket D won')
    rd.shapesize(2.5)
    #color('black')
    write.write('Rocket D won',font=('arail', 32, 'bold'))
    for i in range(72):
        rd.right(5)
        rd.shapesize(2.5)


turtle.done()