from abc import ABC, abstractmethod

class Hospital:
    def __init__(self, razonSocial):
        self.razonSocial = razonSocial
        self.atenciones = []

    def agregar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def importe_total_atencion_consulta(self):
        importeTotal = 0
        for consulta in self.atenciones:
            if isinstance(consulta, AtencionMedica):
                importeTotal += consulta.calcular_importe_a_cobrar()
        return importeTotal
    
    def importe_promedio_atenciones(self, valorInf, valorSup):
        acuImporte = 0
        contImporte = 0
        for consulta in self.atenciones:
            if isinstance(consulta, AtencionMedica) & (valorInf <= consulta.calcular_importe_a_cobrar() <= valorSup):
                acuImporte += consulta.calcular_importe_a_cobrar()
                contImporte += 1
        return round((acuImporte / contImporte), 2)
    
    def codigo_primera_atencion_habitual(self):
        for consulta in self.atenciones:
            if isinstance(consulta, AtencionMedica) & consulta.paciente.esHabitual:
                return consulta.codigo
        return 0


"""
* En clase Hospital se requiere la implementación de los siguientes métodos:
    * importe_total_atencion_consulta: debe calcular la suma de los importes de las consultas de las atenciones médicas.
    * importe_promedio_atenciones: debe calcular el promedio de los importes a cobrar por aquellas atenciones médicas cuyo importe a 
    cobrar se encuentre entre dos valores recibidos como parámetros.
    * codigo_primera_atencion_habitual: debe retornar el código de la primera atención médica que se haya registrado para un paciente 
    habitual, o 0 si no existe ninguna.
"""

"""
* Cada atención tiene los siguientes datos: un código numérico que identifica a cada atención; y un valor numérico que representa el 
tipode cobro (1: “efectivo”; 2: “tarjeta de crédito”). Las atenciones pueden ser médicas o de farmacia:
    * Una atención médica agrega los siguientes datos: el paciente atendido; y el importe de la consulta.
    * Una atención de farmacia agregan los siguientes datos: el importe total de los medicamentos vendidos en dicha atención; y un 
    cupón de descuento que especifica el monto de descuento que se aplicaría sobre el importe total de los medicamentos; en caso que 
    el cupón de descuento sea igual que 0, no se realizará ningún descuento; cabe aclarar que el cupón de descuento debe ser 0 o 
    positivo.
    * Del paciente asociado a la atención médica se registran: su nombre; el síntoma que prevalece (1: “corazon”, 2: “pulmon”, 3: 
    “otras”); y un valor booleano que representa si el paciente es habitual (true) o no (false) del hospital.
""" 
class Atencion(ABC):
    def __init__(self, codigo, tipoCobro: int):
        self.codigo = codigo
        self.tipoCobro = tipoCobro # 1: efectivo, 2: tarjeta de crédito

    @abstractmethod
    def calcular_importe_a_cobrar(self):
        pass

    def __str__(self):
        return f"Código: {self.codigo}, Tipo de Cobro: {self.tipoCobro}"


class AtencionMedica(Atencion):
    def __init__(self, codigo, tipoCobro, paciente, importeConsulta):
        super().__init__(codigo, tipoCobro)
        self.paciente = paciente
        self.importeConsulta = importeConsulta

    def calcular_importe_a_cobrar(self):
        descuento = 0
        if self.paciente.esHabitual:
            descuento = 0.25
        if self.tipoCobro == 2:
            descuento += -0.2
        else:
            descuento += 0.1
        importeFinal = self.importeConsulta - (self.importeConsulta * descuento)

        return importeFinal
    
    def __str__(self):
        return f"{super().__str__()}, Paciente: {self.paciente.nombre}, Importe Consulta: {self.importeConsulta}, Importe a Cobrar: {self.calcular_importe_a_cobrar()}"


class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipoCobro, importeMedicamentos, cuponDescuento):
        super().__init__(codigo, tipoCobro)
        self.importeMedicamentos = importeMedicamentos
        if cuponDescuento >= 0:
            self.cuponDescuento = cuponDescuento
        else:
            self.cuponDescuento = 0

    def calcular_importe_a_cobrar(self):
        # Se asume que se pasarán valores como porcentajes, ej: 10, 20, 30
        descuento = self.cuponDescuento * 0.01
        if self.tipoCobro == 2:
            descuento += -0.3
        else:
            descuento += 0.05
        importeFinal = self.importeMedicamentos - (self.importeMedicamentos * descuento)

        if (importeFinal < 0):
            return 0
        return importeFinal


    def __str__(self):
        return f"{super().__str__()}, Importe Medicamentos: {self.importeMedicamentos}, Cupón: {self.cuponDescuento}, Importe a Cobrar: {self.calcular_importe_a_cobrar()}"


class Paciente():
    def __init__(self, nombre, sintoma, esHabitual: bool):
        self.nombre = nombre
        self.sintoma = sintoma # 1: corazon, 2: pulmon, 3: otras
        self.esHabitual = esHabitual # True o False

    def __str__(self):
        sintoma = ""
        if self.sintoma == 1:
            sintoma = "corazon"
        elif self.sintoma == 2:
            sintoma = "pulmon"
        else:
            sintoma = "otras"
        return f"Nombre: {self.nombre}, Sintoma: {sintoma}, Es Habitual: {self.esHabitual}"