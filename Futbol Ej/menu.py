from classPlayer import *
from classTeam import *
import pandas as pd

teams_list = []


def pichichis(teams_list):
    goals=[]
    namePlayers=[]
    c=0
    for n in range(len(teams_list)):
        for x in teams_list[c].jugadores:
            goals.append(x.goles)
            namePlayers.append(x.nombre)
        c +=1
    goalsTable={
        "Jugadores":namePlayers,
        "Goles":goals
    }
    df = pd.DataFrame(goalsTable)
    df_sorted=df.sort_values(by='Goles',ascending=False)

    print(df_sorted.head(5))

    return


def test_score(user_input):
    if len(user_input)!=3 or user_input[1]!=" ":
        print("introduce el resultado siguiendo el formato: GolesLocal espacio GolesVisitante")
        return (10)
    else:
        try:
            if int(user_input[0]) or int(user_input[2]):
                return (user_input)
            else:
                print("introduce el resultado siguiendo el formato: GolesLocal espacio GolesVisitante")
                return (10)
        except ValueError:
            print("introduce el resultado siguiendo el formato: GolesLocal espacio GolesVisitante")
            return (10)

def test_visitorTeam(user_input,min,max,visitor):
    range_1= range(min,max+1,1)
    try:
         if int(user_input) in range_1 and int(visitor)!=int(user_input):
            return (int(user_input))
         else:
            print("introduce un numero dentro del rango y que no sea igual que el local")
            return (10)
    except ValueError:
        print("introduce un numero dentro del rango")
        return (10)

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

def show_teams(num):
    if len(teams_list)<=num:
        print("introduce primero los equipos necesarios")
        return (0)
    else:
        n=0
        for x in teams_list:
            n+=1
            (print("{}-".format(n)+x.nombre))


def compete (teams_list):
    if show_teams(1)==0:
        return
    else:

        print("¿Cuales es el local?")
        localTeam=10
        while localTeam==10:
            localTeam = test_input(input(),1,len(teams_list))
        localTeam=localTeam-1

        print("¿Cuales es el visitante?")
        visitorTeam=10
        while visitorTeam==10:
            visitorTeam = test_visitorTeam(input(),1,len(teams_list),localTeam+1)
        visitorTeam=visitorTeam-1

        print("¿Como han quedado?")
        score=10
        while score==10:
             score = test_score(input())
        localGoals=int(score[0])
        visitorGoals=int(score[2])
        if localGoals>visitorGoals:
            teams_list[localTeam].winner()
            teams_list[visitorTeam].loser()
        elif localGoals<visitorGoals:
            teams_list[visitorTeam].winner()
            teams_list[localTeam].loser()
        else:
            teams_list[visitorTeam].draw()
            teams_list[localTeam].draw()
        while localGoals!=0:
            print("¿Quien ha metido gol en el equipo local?")
            n=0
            for x in teams_list[localTeam].jugadores:
                print("{}-".format(n)+x.nombre)
                n+=1
            playerSelected=10
            while playerSelected==10:
             playerSelected = test_input(input(),0,len(teams_list[localTeam].jugadores)-1)
            playerSelected = int(playerSelected)
            teams_list[localTeam].jugadores[playerSelected].goles += 1
            localGoals-=1

        while visitorGoals!=0:
            print("¿Quien ha metido gol en el equipo visitante?")
            n=0
            for x in teams_list[visitorTeam].jugadores:
                print("{}-".format(n)+x.nombre)
                n+=1
            playerSelected=10
            while playerSelected==10:
             playerSelected = test_input(input(),0,len(teams_list[visitorTeam].jugadores)-1)
            playerSelected = int(playerSelected)
            teams_list[visitorTeam].jugadores[playerSelected].goles += 1
            visitorGoals-=1

        return (teams_list)


def add_player ():
    if show_teams(0)==0:
        return
    else:
        print("Escoge el número del equipo que quieres añadir jugador")
        teamSelected=10
        while teamSelected==10:
                teamSelected = test_input(input(),1,len(teams_list))

        print("Introduce el nombre del jugador")
        name = input()
        new_player = Player(name, 0)
        team = teams_list[teamSelected- 1]
        team.addPlayer(new_player)
        print(teams_list)

def add_team ():
    print("Escoge Nombre del Equipo")
    newName=input()
    teams_list.append(Team(newName))


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
            menu()
        else:
           add_team()
        menu()

    elif user_input==2:
            add_player()
            menu()

    elif user_input==3:
        for n in range(len(teams_list)):
            if teams_list[n].numPlayers() == 0:
                print ("Añada primero al menos un jugador en cada equipo")
                menu()
            #print(teams_list[n].jugadores[0].nombre)
        compete(teams_list)
        menu()

    elif user_input==5:
            pichichis(teams_list)
            menu()
menu()