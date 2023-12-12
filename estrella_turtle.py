import turtle
from turtle import *

num_puntas = int(input("Introduzca un numero puntas: "))
longitud = 100
while num_puntas < 5:
    print("El número de puntas debe ser al menos 5.")
    num_puntas = int(input("Introduzca un numero puntas: "))


def dibujar_estrella():
    turtle.speed(2)  # Establece la velocidad del turtle (puedes ajustarla según desees)
    turtle.color("green")  # Establece el color de la tortuga
    turtle.bgcolor("black")  # Establece el color del fondo
    turtle.penup()  # Levanta el lápiz (turtle no dibujará)
    turtle.goto(0, 0)  # Mueve el turtle a la posición (100, 0)
    turtle.pendown() # Baja el lápiz (turtle comenzará a dibujar)

    # Calcula el ángulo interior de la estrella
    if num_puntas % 2 == 0:
        # Ajuste para números pares
        angulo = 180 - (360 / num_puntas)
    else:
        angulo = 180 - (180 / num_puntas)  

    for _ in range(num_puntas):
            turtle.forward(longitud)  # Avanza la longitud 
            turtle.right(angulo)  # Gira según el ángulo calculado
    turtle.done()

dibujar_estrella()
