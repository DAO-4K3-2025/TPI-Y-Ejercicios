""" Un partido de fútbol se juega entre dos equipos denominados local y visitante. Desarrollar una clase Partido que
contenga referencias a dos objetos de la clase Equipo. La clase Partido debe poseer atributos para registrar ademas la
cantidad de goles realizada por cada equipo y métodos para informar cuál es el ganador o si hubo empate. Por otro
lado, la clase Equipo debe poseer un método RegistrarPartido que reciba por parámetro un partido y asigne atributos
(almacenados o calculados) para informar: 

Cantidad de partidos jugados
Cantidad de partidos jugados como local
Cantidad de partidos jugados como visitante
Suma de goles realizados
Suma de goles recibidos
Diferencia total de goles
Cantidad de partidos ganados
Cantidad de partidos empatados
Cantidad de partidos recibidos
Sumatoria de puntos (suponiendo que todos los partidos son de un mismo campeonato)
"""

#from partido import Partido

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidos = []
        self._cantPartidosLocal = 0
        self._cantPartidosVisitante = 0
        self._golesRealizados = 0
        self._golesRecibidos = 0


    def registrar_partido(self, partido):
        self.partidos.append(partido)
    
    def agregar_gol_realizado(self, goles):
        self._golesRealizados += goles

    def agregar_gol_recibido(self, goles):
        self._golesRecibidos += goles

    # Cantidad de partidos jugados
    def contar_partidos(self):
        return len(self.partidos)

    # Cantidad de partidos jugados como local
    def contar_partidos_local(self):
        cont = 0
        for partido in self.partidos:
            if partido.equipoLocal.nombre == self.nombre:
                cont += 1
        return cont
    
    # Cantidad de partidos jugados como visitante
    def contar_partidos_visitante(self):
        cont = 0
        for partido in self.partidos:
            if partido.equipoVisitante.nombre == self.nombre:
                cont += 1
        return cont

    # Suma de goles realizados
    def goles_realizados(self):
        return self._golesRealizados

    # Suma de goles recibidos
    def goles_recibidos(self):
        return self._golesRecibidos
    
    # Diferencia total de goles
    def diferencia_goles(self):
        return abs(self._golesRealizados - self._golesRecibidos)
    
    # Cantidad de partidos ganados
    def partidos_ganados(self) -> int:
        cont = 0
        for partido in self.partidos:
            if partido.ganador == self.nombre:
                cont += 1
        return cont
        
    # Cantidad de partidos empatados
    def partidos_empatados(self):
        cont = 0
        for p in self.partidos:
            if p.ganador == "Empate":
                cont += 1
        return cont
    
    # Cantidad de partidos recibidos

    def mostrar_partidos(self):
        if not self.partidos:
            return "No hay partidos guardados"
        else:
            return "\n".join([str(p) for p in self.partidos])

    def __str__(self):
        return f"Nombre: {self.nombre}\nPartidos:\n{self.mostrar_partidos()}"
