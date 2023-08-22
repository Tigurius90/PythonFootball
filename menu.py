from add_player import *
from classEquipo import *
from add_team import *

teams_list=[]

def test_input(user_input,min,max):
    range_1= range(min,max+1,1)
    try:
         if int(user_input) in range_1:
            return (int(user_input))
         else:
            print("introduce un numero numero dentro del rango")
            return (10)
    except ValueError:
        print("introduce un numero numero dentro del rango")
        return (10)
    
def show_teams(teams_list,num): 
    if len(teams_list)<=num:
        print("introduce primero los equipos necesarios")
        return (0)
    else:
        n=0
        for x in teams_list:
            n+=1
            (print("{}-".format(n)+x.nombre))


def competir (teams_list):
    if show_teams(teams_list,1)==0:
        return
    else:
        print("¿Cuales es el local?")
        equipo_local=10
        while equipo_local==10:
            equipo_local = test_input(input(),1,len(teams_list)) - 1
        print("¿Cuales es el visitante?")   
        equipo_visitante=10
        while equipo_visitante==10:
            equipo_visitante = test_input(input(),1,len(teams_list)) - 1

        return (teams_list)
    

def add_player (teams_list):
    if show_teams(teams_list,0)==0:
        return
    else:
        print("Escoge el número del equipo que quieres añadir jugador")
        teamSelected=10
        while teamSelected==10:
                teamSelected = test_input(input(),1,len(teams_list))

        print("Introduce el nombre del jugador")
        teams_list[teamSelected- 1].jugadores.append(Player(input(),""))
        # para testear - cirstobal, hay alguna otra manera de verlo? print (teams_list[0].jugadores[0].nombre)

        return (teams_list)
    

def add_team (teams_list):
    print("Escoge Nombre del Equipo")
    newName=input()
    teams_list.append(Team(newName,[],"","",""))
    return (teams_list)


def menu ():
    global teams_list
    options=["0 - Salir", "1- Añadir equipo","2- Añadir jugador","3- Competir","4- Clasificación","5- Pichichis"]
    for x in options: 
        print (x)

# Chequea que no sea un numero del menu
    user_input=10
    while user_input==10:
        user_input=test_input(input("escoge número de la opción de arriba : "),0,5)

    if user_input==0:
        print("Hasta la vista")
        exit()
    elif user_input==1: 
        if len(teams_list) > 4:
            print ("Numero de equipos excedido, elija otra opcion")
            return menu()
        else:
           teams_list= add_team(teams_list)
        menu()

    elif user_input==2:
            teams_list=add_player(teams_list)
            menu()

    elif user_input==3:
            competir(teams_list)
            menu()
menu()