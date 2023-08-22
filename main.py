from funciones import *
from añadir_equipo import *
from clases import *

global EquiposAñadidos
global lista_equipos
lista_equipos=[]

def main ():
    menu=["0 - Salir", "1- Añadir equipo","2- Añadir jugador","3- Competir","4- Clasificación","5- Pichichis"]
    print("escoge número de la opción") 
    for x in menu: 
        print (x)

# Chequea que no sea un numero del menu
    user_input=testea_numero_menu(input())

    if user_input==0:
        print("Hasta la vista")
        exit()

    elif user_input==1:
        EquiposAñadidos = + 1
        if EquiposAñadidos > 4:
            print ("Numero de equipos excedido, elija otra opcion")
            return main()
        else:
            añadir_equipo(lista_equipos)
            print(lista_equipos[0].nombre)
main()