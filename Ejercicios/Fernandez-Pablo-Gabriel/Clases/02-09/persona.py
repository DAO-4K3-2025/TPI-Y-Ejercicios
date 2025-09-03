class Persona:

    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


    def __str__(self):
        return "Nombre: " + self.nombre + " | Edad: " + str(self.edad) + " | DNI: " + str(self.dni)
    
    def es_mayor_edad(self):
        return self.edad >= 18