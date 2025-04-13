# Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.

import turtle

def polygon(t, n, lenght):
    angle = 360 / n
    for _ in range(n):
        t.forward(lenght)
        t.right(angle)

bob = turtle.Turtle()
polygon(bob, 10, 50)

turtle.done()