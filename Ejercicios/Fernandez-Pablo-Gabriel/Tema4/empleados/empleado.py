"""
* Tipo de empleado (1: obrero, 2: administrativo, 3: vendedor).
* Legajo
* Nombre
* Apellido
* Sueldo básico
* La sexta columna depende del tipo de empleado, en el caso de los obreros indica la cantidad de días trabajados en el mes, 
  en el caso de los administrativos indica si le corresponde cobrar presentismo y en el caso de los vendedores indica el 
  importe total de ventas realizadas en mes.

Por cada tipo de empleados el sueldo se calcula de una forma diferente:
* En el caso de los obreros, el sueldo básico corresponde a un mes de 20 días laborables, y el sueldo a cobrar debe ser un 
  propocional a la cantidad de días efectivamente trabajados.
* En el caso de los administrativos, el sueldo a cobrar es igual al básico, pero se incrementa en 13% si le corresponde 
  cobrar el presentismo.
* Los vendedores cobrar el sueldo básico más un 1% del total vendido.

Luego de la carga:
* Calcular el total a pagar de sueldos
* Contar los empleados por tipo (tres totales)
* Buscar un empleado por legajo y mostrar el sueldo a pagar 
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, legajo, nombre, apellido, sueldoBase):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldoBase = sueldoBase
    
    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def devolver_tipo(self):
        pass

    def __str__(self):
        return f"Nombre Completo: {self.nombre} {self.apellido} | Sueldo Base: {self.sueldoBase}"

#-------------------------------------------------------------------------------------
class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldoBase, diasTrabajados):
        super().__init__(legajo, nombre, apellido, sueldoBase)
        self.diasTrabajados = diasTrabajados

    def calcular_sueldo(self):
        sueldoFinal = (self.sueldoBase * self.diasTrabajados) / 20
        return sueldoFinal
    
    def devolver_tipo(self):
        return "Obrero"
    
    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.devolver_tipo()} | Sueldo Final: {self.calcular_sueldo()}"

#-------------------------------------------------------------------------------------
class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldoBase, cobrarPresentismo):
        super().__init__(legajo, nombre, apellido, sueldoBase)
        self.cobrarPresentismo = cobrarPresentismo

    def calcular_sueldo(self):
        if self.cobrarPresentismo == 'true':
            return self.sueldoBase * 1.13
        return self.sueldoBase

    def devolver_tipo(self):
        return "Administrativo"
    
    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.devolver_tipo()} | Sueldo Final: {self.calcular_sueldo()}"

#-------------------------------------------------------------------------------------
class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldoBase, totalVentas):
        super().__init__(legajo, nombre, apellido, sueldoBase)
        self.totalVentas = totalVentas

    def calcular_sueldo(self):
        return (self.totalVentas * 0.01) + self.sueldoBase
    
    def devolver_tipo(self):
        return "Vendedor"
    
    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.devolver_tipo()} | Sueldo Final: {self.calcular_sueldo()}"