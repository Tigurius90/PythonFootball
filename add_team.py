from classEquipo import Team

def add_team (teams_list):
    print("Escoge Nombre del Equipo")
    newName=input()
    teams_list.append(Team(newName,[],"","",""))
    return (teams_list)