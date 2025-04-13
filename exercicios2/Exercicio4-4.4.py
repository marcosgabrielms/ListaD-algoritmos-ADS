# As letras do alfabeto podem ser construídas a partir de um número moderado de elementos básicos, como linhas verticais e horizontais e algumas curvas. 
# Crie um alfabeto que possa ser desenhado com um número mínimo de elementos básicos e então escreva funções que desenhem as letras.

import turtle

# Configura a tartaruga
def setup_turtle(t):
    t.setheading(0)
    t.pendown()

# Letra A
def draw_a(t):
    setup_turtle(t)
    t.left(75)
    t.forward(50)
    t.right(150)
    t.forward(50)
    t.backward(25)
    t.left(75)
    t.forward(20)
    t.penup()
    t.setheading(0)
    t.forward(40)

# Letra B
def draw_b(t):
    setup_turtle(t)
    t.left(90)
    t.forward(50)
    t.right(90)
    for _ in range(18):
        t.forward(1)
        t.right(10)
    t.left(180)
    for _ in range(18):
        t.forward(1)
        t.right(10)
    t.penup()
    t.setheading(0)
    t.forward(40)

# Letra C (agora correta para sentido normal)
def draw_c(t):
    setup_turtle(t)
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
    for _ in range(18):
        t.forward(1.5)
        t.left(10)
    t.penup()
    t.setheading(0)
    t.forward(20)

# Letra D
def draw_d(t):
    setup_turtle(t)
    t.left(90)
    t.forward(50)
    t.right(90)
    for _ in range(36):
        t.forward(1.5)
        t.right(5)
    t.penup()
    t.setheading(0)
    t.forward(40)

# Letra E
def draw_e(t):
    setup_turtle(t)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.penup()
    t.backward(20)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(15)
    t.penup()
    t.backward(15)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(0)
    t.forward(40)

# Escreve uma palavra da esquerda pra direita
def escreve(t, palavra):
    for letra in palavra.lower():
        if letra == 'a':
            draw_a(t)
        elif letra == 'b':
            draw_b(t)
        elif letra == 'c':
            draw_c(t)
        elif letra == 'd':
            draw_d(t)
        elif letra == 'e':
            draw_e(t)
        else:
            t.penup()
            t.forward(40)

# Main
def main():
    tela = turtle.Screen()
    tela.bgcolor("black")

    t = turtle.Turtle()
    t.color("cyan")
    t.pensize(2)
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    escreve(t, "ABCDE")

    turtle.done()

main()
