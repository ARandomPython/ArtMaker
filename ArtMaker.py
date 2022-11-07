from turtle import *
tom = Turtle()
tom.shape('turtle')
bgcolor('coral')

def movFor():
    tom.fd(25)

def movLeft():
    tom.lt(45)

def uno():
    tom.undo()

def notDraw():
    tom.pu()

def draw():
    tom.pd()

screen = Screen()
screen.listen()

onkey(key='space', fun=movFor)
onkey(key='a', fun=movLeft)
onkey(key='u', fun=uno)
onkey(key='s', fun=notDraw)
onkey(key='t', fun=draw)