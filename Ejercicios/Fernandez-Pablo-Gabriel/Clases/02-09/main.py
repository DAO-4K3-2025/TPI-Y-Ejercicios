""" class Auto:
    def __init__(self,patente,color,marca):
        self.patente = patente
        self.color = color
        self.marca = marca


    def __str__(self):
        return "patente: " + self.patente + " | color: " + self.color + " | marca: " + self.marca
    



def main():
    # Indica la clase para instanciar, luego llama el constructor pidiendo los valores necesarios.
    print("Ingrese los valores del mdfkin auto:")
    for i in range(3):
        print("Auto", i)
        patente = input("Ingrese patente: ")
        color = input("Ingrese color: ")
        marca = input("Ingrese marca: ")
        auto = Auto(patente, color, marca)
        print(auto)
        print("-" * 50) """


    

""" class Persona:

    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


    def __str__(self):
        return "Nombre: " + self.nombre + " | Edad: " + str(self.edad) + " | DNI: " + str(self.dni)
    
    def es_mayor_edad(self):
        return self.edad > 18 """

from persona import Persona
from cuenta import Cuenta

def main():
    # Indica la clase para instanciar, luego llama el constructor pidiendo los valores necesarios.
    print("Valores personas")
    per1 = Persona("Pablo", 22, 44568100)
    cue1 = Cuenta(per1, 10000)

    print(per1)
    print("Es mayor de edad:", per1.es_mayor_edad())

    print(cue1)
    print(cue1.monto)
    cue1.depositar(2000)
    print(cue1.monto)
    print(cue1.extraer(9000))
    print(cue1.monto)
    print(cue1.extraer(9000))
    print(cue1.monto)

    """ print("Ingrese los valores del persona:")
    for i in range(3):
        print("Persona", i)
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        dni = int(input("Ingrese dni: "))
        persona = Persona(nombre, edad, dni)
        print(persona)
        print("Es mayor de edad:", persona.es_mayor_edad())
        print("-" * 50) """



if __name__ == "__main__":
    main()