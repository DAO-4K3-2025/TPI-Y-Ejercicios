""" Un partido de fútbol se juega entre dos equipos denominados local y visitante. Desarrollar una clase Partido que
contenga referencias a dos objetos de la clase Equipo. La clase Partido debe poseer atributos para registrar ademas la
cantidad de goles realizada por cada equipo y métodos para informar cuál es el ganador o si hubo empate. Por otro
lado, la clase Equipo debe poseer un método RegistrarPartido que reciba por parámetro un partido y asigne atributos
(almacenados o calculados) para informar: """
from equipo import Equipo

class Partido:
    def __init__(self, equipoVisitante: Equipo, equipoLocal: Equipo, golesVisitante, golesLocal):
        self._equipoLocal = equipoLocal
        self._equipoVisitante = equipoVisitante
        self._golesVisitante  = golesVisitante
        self._golesLocal = golesLocal
        self.equipoVisitante = equipoVisitante
        self.equipoLocal = equipoLocal
        self.ganador = self.nombre_ganador()
        self.asignar_partido()

    @property
    def golesVisitante(self):
        return self._golesVisitante
    
    @golesVisitante.setter
    def golesVisitante(self, goles):
        self.golesVisitante = goles
    
    @property
    def golesLocal(self):
        return self._golesLocal
    
    @golesLocal.setter
    def golesLocal(self, goles):
        self.golesLocal = goles

    def nombre_ganador(self) -> str:
        if self.golesLocal > self.golesVisitante:
            return str(self.equipoLocal.nombre)
        elif self.golesLocal < self.golesVisitante:
            return str(self.equipoVisitante.nombre)
        else:
            return "Empate"

    def asignar_partido(self):
        self.equipoLocal.registrar_partido(self)
        self.equipoLocal.agregar_gol_realizado(self.golesLocal)
        self.equipoLocal.agregar_gol_recibido(self.golesVisitante)

        self.equipoVisitante.registrar_partido(self)
        self.equipoVisitante.agregar_gol_realizado(self.golesVisitante)
        self.equipoVisitante.agregar_gol_recibido(self.golesLocal)

    def __str__(self):
        return f"Visitante: {self.equipoVisitante.nombre} | Local: {self.equipoLocal.nombre} | Goles: {self.golesVisitante}-{self.golesLocal}"
        



