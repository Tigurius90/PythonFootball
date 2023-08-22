from funciones import *
from añadir_equipo import *
from clases import *
from añadir_jugador import *
from competir import *

global lista_equipos
lista_equipos=[]

def main ():
    menu=["0 - Salir", "1- Añadir equipo","2- Añadir jugador","3- Competir","4- Clasificación","5- Pichichis"]
    print("escoge número de la opción") 
    for x in menu: 
        print (x)

# Chequea que no sea un numero del menu
    user_input=testea_numero_menu(input(),5,0)

    if user_input==0:
        print("Hasta la vista")
        exit()

    elif user_input==1:
        if len(lista_equipos) > 4:
            print ("Numero de equipos excedido, elija otra opcion")
            return main()
        else:
            añadir_equipo(lista_equipos)
            main()

    elif user_input==2:
            añadir_jugador(lista_equipos)
            main()

    elif user_input==3:
            competir(lista_equipos)
            main()
main()