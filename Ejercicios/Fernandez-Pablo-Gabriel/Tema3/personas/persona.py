""" Programar una clase Persona con atributos suficientes para almacenar documento, nombre,
apellido y edad de una persona.  """

class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self._edad = edad
    
    def __str__(self):
        return f'DNI: {self.documento} | Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad}'
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, n_edad):
        self._edad = n_edad

    def __lt__(self, persona):
        return (self.edad < persona.edad)
