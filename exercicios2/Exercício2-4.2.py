# Escreva um conjunto de funções adequadamente geral que possa desenhar flores como as da Figura 4.1

import turtle
import math

# Função para desenhar um arco (parte de círculo)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1  # número de segmentos
    step_length = arc_length / n
    step_angle = angle / n

    # Inclina o turtle para alinhar com a curva 
    t.left(step_angle / 2)
    
    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

    # Volta a inclinação inicial
    t.right(step_angle / 2)

# Função para desenhar uma pétala da flor
def petal(t, r, angle):
    for _ in range(2):  # Desenha uma pétala com dois arcos
        arc(t, r, angle)
        t.left(180 - angle)

# Função para desenhar a flor completa
def flower(t, n_petals, r, angle):
    for _ in range(n_petals):
        petal(t, r, angle)
        t.left(360 / n_petals)

def caule(t, length):
    t.right(90)
    t.forward(length)        

def desenha_nome(t, name):
    t.penup()
    t.goto(150, -100)
    t.pendown()
    t.write(name, font=("Arial", 24, "normal"))    

# Main do turtle
def main():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Define o fundo da tela

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("yellow")    # Cor da tartaruga (pode mudar para qualquer cor em inglês)
    bob.speed(0)            # Velocidade do Bob

    # Desenha a flor
    flower(bob, n_petals=12, r=100, angle=60)

    bob.penup()
    bob.goto(0, -10)
    bob.pendown()
    bob.color("green")
    caule(bob, length=200)
    desenha_nome(bob, "Marcos Gabriel")

    turtle.done()

# Executa o programa
main()
  