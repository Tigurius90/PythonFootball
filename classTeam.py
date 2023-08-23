class Team:
        
    ganados = 0
    perdidos = 0
    empatados = 0
    jugadores = []

    def __init__(self, nombre):
            self.nombre=nombre
    def winner(self):
            self.ganados +=1
    def loser(self):
            self.perdidos +=1
    def draw(self):
            self.empatados +=1
    def numPlayers(self):
           return (len(self.jugadores))