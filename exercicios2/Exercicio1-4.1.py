# Desenhe um diagrama da pilha que mostre o estado do programa enquanto executa circle (bob, radius). 
# Você pode fazer a aritmética à mão ou acrescentar instruções print ao código.

import turtle
import math
import time  # Sleep para pausar a execução do programa para seguir pro próximo desenho

def polygon(t, n, length):
    print("Entrou em polygon()")
    print(f"  t = {t}")
    print(f"  n = {n}")
    print(f"  length = {length:.2f}")
    angle = 360 / n
    for i in range(n):
        print(f"  Lado {i+1}: t.forward({length:.2f})")
        t.forward(length)
        print(f"  t.right({angle:.2f})")
        t.right(angle)
    print("Saindo de polygon()\n")

def circle(t, r):
    print("Entrou em circle()")
    print(f"  t = {t}")
    print(f"  r = {r:.2f}")
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n  
    print(f"  Circunferência = {circumference:.2f}")
    print(f"  Usando n = {n}, então length = {length:.2f}")
    print("Chamando polygon() de dentro de circle()\n")
    polygon(t, n, length)
    print("Saindo de circle()\n")

# Programa principal
print("Início do programa principal\n")
bob = turtle.Turtle()

# Desenha o polígono
polygon(bob, 6, 70)

# Mensagem com pausa antes do círculo
print("Polígono concluído. Agora começando o círculo...\n")
time.sleep(2)  # Pausa de 2 segundos


bob.penup()
bob.goto(28, 200) # Posição X/Y dos desenhos do Bob
bob.setheading(0)
bob.pendown()


circle(bob, 100) # desenha círculo

print("Fim do programa principal")
turtle.done()
