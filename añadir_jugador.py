from clases import equipo
from clases import jugador
from funciones import testea_numero_menu

def añadir_jugador (lista_equipos):
    if len(lista_equipos)==0:
        print("introduce primero un jugador")
        return (lista_equipos)
    else:
        n=0
        print("Escoge el número del equipo que quieres añadir jugador")
        for x in lista_equipos:
            n+=1
            print("{}-".format(n)+x.nombre)
        equipo_seleccionado = testea_numero_menu(input(),1,len(lista_equipos)) - 1

        print("Nombre del jugador")
        lista_equipos[equipo_seleccionado].jugadores.append(jugador(input(),""))
        # para testear - cirstobal, hay alguna otra manera de verlo? print (lista_equipos[0].jugadores[0].nombre)

        return (lista_equipos)

