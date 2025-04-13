import turtle

def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

bob = turtle.Turtle() # Criação da tartaruga
square(bob, 250)
turtle.done()