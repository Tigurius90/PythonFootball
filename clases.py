class equipo:
    def __init__(self, nombre, jugadores, ganados, perdidos, empatados):
        self.jugadores=jugadores
        self.nombre= nombre
        self.ganados= ganados
        self.perdidos= perdidos
        self.empatados= empatados


class jugador:
     def __init__(self, nombre, posición):
        self.posición=posición
        self.nombre= nombre