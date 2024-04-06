import turtle
from turtle import *

wn = Screen()
wn.bgcolor('green')
t = turtle.Turtle()
t.pencolor('white')

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    