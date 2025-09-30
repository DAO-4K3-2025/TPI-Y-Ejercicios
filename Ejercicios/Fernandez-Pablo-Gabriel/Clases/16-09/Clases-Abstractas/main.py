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


def main():
    gato1 = Gato()
    perro1 = Perro()

    gato1.hacer_sonido()
    perro1.hacer_sonido()


if __name__ == "__main__":
    main()