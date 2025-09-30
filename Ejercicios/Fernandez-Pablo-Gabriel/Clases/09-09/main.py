class Vehiculo():
    color = "Rojo"
    ruedas = 4
    autonomia = 10

    def __init__(self, color, ruedas, autonomia):
        self.color = color
        self.ruedas = ruedas
        self.autonomia = autonomia

    def get_autonomia(self):
        return self.autonomia


class Coche(Vehiculo):
    velocidad = 300
    cilindrada = 1700
    autonomia = 10

    def __init__(self, velocidad, cilindrada, color, ruedas, autonomia):
        super().__init__(color, ruedas, autonomia)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_autonomia(self):
        return  super().get_autonomia() + self.autonomia



def main():
    coche1 = Coche(10, 20, "Azul", 4, 50)
    #bici = Vehiculo("Rojo", 1)

    print(coche1.get_autonomia())


if __name__ == "__main__":
    main()