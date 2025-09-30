from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

# class Pato(Animal):
#     pass

# Ejemplo de uso
perro = Perro()
perro.hacer_sonido()  # Imprime: Guau!

gato = Gato()
gato.hacer_sonido()   # Imprime: Miau!

# pato = Pato()

