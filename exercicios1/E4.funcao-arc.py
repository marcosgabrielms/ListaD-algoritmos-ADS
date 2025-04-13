# Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, 
# para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, 
# então quando angle=360, o arc deve desenhar um círculo completo.

import turtle
import math

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

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * (angle / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for _ in range(n):
        t.forward(step_length)
        t.right(step_angle)


bob = turtle.Turtle()

# circle(bob, 100)         # Círculo completo
#arc(bob, 100, 360)       # Também um círculo completo
arc(bob, 100, 180)       # Semicírculo
#arc(bob, 100, 90)          # 1/4 de círculo

turtle.done()
