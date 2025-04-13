# Escreva um conjunto de funções adequadamente geral que possa desenhar formas como as da Figura 4.2
import turtle
import math

def triangulo_isoceles(t, r, angle):
    base_angle = (180 - angle) / 2
    base_length = 2 * r * math.sin(math.radians(angle / 2))

    
    pos = t.position()          # Salva posição e direção original da tartaruga
    heading = t.heading()

    t.forward(r)
    t.left(180 - base_angle)
    t.forward(base_length)
    t.left(180 - base_angle)
    t.forward(r)

  
    t.setposition(pos)              # Retorna ao centro e à direção original
    t.setheading(heading)

def desenha_torta(t, n, r):
    angle = 360 / n
    for _ in range(n):
        triangulo_isoceles(t, r, angle)
        t.left(angle)

def movimenta_bob(t, distance):
    t.penup()
    t.forward(distance)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("cyan")
    bob.speed(0)
    bob.pensize(1)

    desenha_torta(bob, n=5, r=60)  # Torta de 5 fatias
    movimenta_bob(bob, 150)

    desenha_torta(bob, n=6, r=60)  # Torta de 6 fatias
    movimenta_bob(bob, 150)

    desenha_torta(bob, n=7, r=60)  # Torta de 7 fatias

    turtle.done()

main()
