# Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados.
#  Teste a sua função com uma série de valores de r.

import turtle
import math

def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

def polygon(t, n, length):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


bob = turtle.Turtle()


circle(bob, 150)

turtle.done()
