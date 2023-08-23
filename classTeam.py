class Team:

    def __init__(self, nombre):
        self.nombre=nombre
        self.ganados = 0
        self.perdidos = 0
        self.empatados = 0
        self.jugadores = []
    def winner(self):
            self.ganados +=1
    def loser(self):
            self.perdidos +=1
    def draw(self):
            self.empatados +=1
    def numPlayers(self):
           return (len(self.jugadores))
    def addPlayer(self, player):
        self.jugadores.append(player)