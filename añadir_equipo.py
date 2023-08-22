from clases import equipo

def añadir_equipo (lista_equipos):
    print("Escoge Nombre del Equipo")
    nuevo_nombre=input()
    lista_equipos.append(equipo(nuevo_nombre,"","","",""))
    return (lista_equipos)