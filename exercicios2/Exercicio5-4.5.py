# Leia sobre espirais em https://pt.wikipedia.org/wiki/Espiral; então escreva um programa que desenhe uma espiral de Arquimedes (ou um dos outros tipos).

import turtle
import math

def espiral_arquimedes(t, a=0, b=5, n_voltas=1000):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)
    t.speed(0)  
    

    for i in range(n_voltas):
        theta = math.radians(i)
        r = a + b * theta
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        t.goto(x, y)

def main():
    tela = turtle.Screen()
    tela.bgcolor("black")

    t = turtle.Turtle()
    t.color("cyan")
    t.pensize(2)

    espiral_arquimedes(t, a=0, b=5, n_voltas=720)

    turtle.done()

main()
