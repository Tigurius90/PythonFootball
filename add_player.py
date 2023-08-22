from classPlayer import Player
from menu import test_input
from menu import show_teams

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

