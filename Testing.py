import pandas as pd
class Team:
    def __init__(self, nombre, jugadores, ganados, perdidos, empatados):
        self.jugadores=jugadores
        self.nombre= nombre
        self.ganados= ganados
        self.perdidos= perdidos
        self.empatados= empatados
    def NumPlayers(self):
        return (len(self.jugadores))

class Player:
     def __init__(self, nombre, posición):
        self.posición=posición
        self.nombre= nombre

team1= Team("RealMadrid",[Player("Raul","delantero")],0,0,0)
team2= Team("Pateti",[Player("DiegoCosta","delantero")],0,0,0)
teams_list=[team1,team2]
teams_list[0].jugadores.append(Player("CR7","delantero"))
teams_list[0].jugadores[0].goles =10
teams_list[0].jugadores[1].goles =100
teams_list[1].jugadores[0].goles =5

goals=[]
namePlayers=[]
c=0
for n in range(len(teams_list)):
    for x in teams_list[c].jugadores:
        goals.append(x.goles)
        namePlayers.append(x.nombre)
    c +=1
print(goals)
print(namePlayers)
goalsTable={
    "Jugadores":namePlayers,
    "Goles":goals
}
df = pd.DataFrame(goalsTable)
df_sorted=df.sort_values(by='Goles',ascending=False)

print(df_sorted.head(5))




for n in range(len(teams_list)):
    print(teams_list[n].NumPlayers())
