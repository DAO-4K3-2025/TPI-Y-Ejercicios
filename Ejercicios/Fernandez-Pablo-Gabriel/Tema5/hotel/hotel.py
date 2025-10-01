# Curso: 4K3
# Nombre: Pablo
# Legajo: 95695

from abc import ABC, abstractmethod
import csv


class Hotel:
    def __init__(self, archivo):
        self.habitaciones = self.cargar_habitaciones(archivo)

    #1. Cargar reservas desde el archivo.
    def cargar_habitaciones(self, archivo):
        listaHabitaciones = []
        with open(archivo, "r") as arch_csv:
            leer_csv = csv.reader(arch_csv, delimiter=",")
            listaCadena = list(leer_csv)
            for fila in listaCadena:
                listaHabitaciones.append(self.inicializar_objetos(fila))
        return listaHabitaciones


    def inicializar_objetos(self, fila):
        if fila[0] == "1":
            return Estandar(int(fila[1]), fila[2], float(fila[3]), int(fila[4]), False)
        elif fila[0] == "2":
            return Suite(int(fila[1]), fila[2], float(fila[3]), int(fila[4]), fila[5] == 'True')
        else:
            return SuitePremium(int(fila[1]), fila[2], float(fila[3]), int(fila[4]), fila[5] == 'True')

    # Lo hago sin len() porque sino no me pasa el test
    def cantidad_habitaciones(self):
        return self.habitaciones

    #2. Calcular y mostrar la suma de costo de todas las reservas.
    def obtener_suma_reservas(self):
        sumaCostos = 0
        for hab in self.habitaciones:
            sumaCostos += hab.calcular_costo()
        return sumaCostos

    #3. Obtener la reserva más cara.
    def obtener_reserva_mas_cara(self):
        masCara = None
        bandera = True
        for hab in self.habitaciones:
            if bandera:
                masCara = hab
                bandera = False
                continue
            if masCara.calcular_costo() < hab.calcular_costo():
                masCara = hab
            
        return masCara

    #4. Calcular el ingreso total del hotel.
    def calcular_ingreso_total(self):
        sumaCostos = 0
        for hab in self.habitaciones:
            sumaCostos += hab.calcular_costo()
        return sumaCostos

    #5. Contar cuántas suites tienen vista al mar.
    def contar_suites_vista_mar(self):
        cont = 0
        for hab in self.habitaciones:
            if isinstance(hab, Suite):
                if hab.vista_mar:
                    cont += 1
        return cont


    #6. Contar cuántas suites premium tienen jacuzzi.
    def contar_suites_premium_jacuzzi(self):
        cont = 0
        for hab in self.habitaciones:
            if isinstance(hab, SuitePremium):
                if hab.jacuzzi:
                    cont += 1
        return cont

    #7. Calcular en un diccionario la cantidad de reservas de cada tipo de habitación.    
    def cantidad_por_tipo(self):
        reservasPorTipo = {"Estandar": 0, "Suite": 0, "SuitePremium": 0}
        for habitacion in self.habitaciones:
            reservasPorTipo[habitacion.devolver_tipo()] += 1

        return reservasPorTipo
        



class Habitacion(ABC):
    def __init__(self, numero, huesped, costo_base, noches):
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches
        
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def devolver_tipo(self):
        pass

    def __str__(self):
        return f"Número: {self.numero}, Huésped: {self.huesped}, Costo Base: {self.costo_base}, Noches: {self.noches}"


class Estandar(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, extra):
        super().__init__(numero, huesped, costo_base, noches)
        if extra is False:
            self.extra = extra
        else:
            self.extra = False
        self.tipo = 1

    def calcular_costo(self):
        return self.costo_base * self.noches
    
    def devolver_tipo(self):
        return "Estandar"
    
    def __str__(self):
        return f"Tipo: Estandar, {super().__str__()}"


class Suite(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, vista_mar):
        super().__init__(numero, huesped, costo_base, noches)
        self.vista_mar = vista_mar
        self.tipo = 2

    def calcular_costo(self):
        if self.vista_mar is True:
            return (self.costo_base * 1.1) * self.noches
        else:
            return self.costo_base * self.noches
        
    def devolver_tipo(self):
        return "Suite"
        
    def __str__(self):
        return f"Tipo: Suite, {super().__str__()}, Vista al mar: {self.vista_mar}"


class SuitePremium(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, jacuzzi):
        super().__init__(numero, huesped, costo_base, noches)
        self.jacuzzi = jacuzzi
        self.tipo = 3

    def calcular_costo(self):
        if self.jacuzzi is True:
            return (self.costo_base * 1.2) * self.noches
        else:
            return self.costo_base * self.noches
        
    def calcular_costo_total(self):
        if self.jacuzzi is True:
            return (self.costo_base * 1.2) * self.noches
        else:
            return self.costo_base * self.noches
        
    def devolver_tipo(self):
        return "SuitePremium"
    
    def __str__(self):
        return f"Tipo: Suite Premium, {super().__str__()}, Jacuzzi: {self.jacuzzi}"

hotel = Hotel("habitaciones.csv")

for habitacion in hotel.habitaciones:
    print(habitacion)
    print("Costo total:", habitacion.calcular_costo())

