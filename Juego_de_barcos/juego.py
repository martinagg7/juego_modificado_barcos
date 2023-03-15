
import random
from clases.Barco import Barco
def barcos_juego():
    barcos = [
        Barco("Portaaviones", 5), # 5 casillas de largo
        Barco("Acorazado", 4), # 4 casillas de largo
        Barco("Crucero", 3), # 3 casillas de largo
        Barco("Submarino", 3), # 3 casillas de largo
        Barco("Destructor", 2) # 2 casillas de largo
    ]
    barcos_enemigo = [
        Barco("Portaaviones", 5),
        Barco("Acorazado", 4),
        Barco("Crucero", 3),
        Barco("Submarino", 3),
        Barco("Destructor", 2)
    ]
    barcos_jugador = [
        Barco("Portaaviones", 5),
        Barco("Acorazado", 4),
        Barco("Crucero", 3),
        Barco("Submarino", 3),
        Barco("Destructor", 2)
    ]





def jugar():
    print("Bienvenido al juego de barcos")
    print("Debe hundir todos los barcos del enemigo")
    print("Para disparar, introduzca las coordenadas donde desee efectuarlo")
    print("Las coordenadas van de 0 a 9")
    empezar = input("¿Desea empezar el juego? (s/n): ")
    if empezar == "s":
        barcos_juego()
    else:
        print("Gracias por jugar")