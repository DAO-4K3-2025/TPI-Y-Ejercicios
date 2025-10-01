""" 
Un hospital de nuestra ciudad necesita conocer cierta información respecto a los importes cobrados por las distintas atenciones que 
realiza,y requiere de un sistema orientado a objetos que le dé soporte a ello. Los datos relevantes son los siguientes:

* Del Hospital sólo interesa registrar la razón social; y una colección con todas las atenciones realizadas.
* Cada atención tiene los siguientes datos: un código numérico que identifica a cada atención; y un valor numérico que representa el 
tipode cobro (1: “efectivo”; 2: “tarjeta de crédito”). Las atenciones pueden ser médicas o de farmacia:
    * Una atención médica agrega los siguientes datos: el paciente atendido; y el importe de la consulta.
    * Una atención de farmacia agregan los siguientes datos: el importe total de los medicamentos vendidos en dicha atención; y un 
    cupón de descuento que especifica el monto de descuento que se aplicaría sobre el importe total de los medicamentos; en caso que 
    el cupón de descuento sea igual que 0, no se realizará ningún descuento; cabe aclarar que el cupón de descuento debe ser 0 o 
    positivo.
    * Del paciente asociado a la atención médica se registran: su nombre; el síntoma que prevalece (1: “corazon”, 2: “pulmon”, 3: 
    “otras”); y un valor booleano que representa si el paciente es habitual (true) o no (false) del hospital.
    
De cada clase de atención se debe calcular un importeACobrar en pesos, que representa lo que el hospital cobra al paciente por la 
atención brindada. Este cálculo dependerá del tipo de cobro de la atención y de la clase de atención brindada:

* El importe total de las atenciones médicas se calcula a partir del importe de la consulta. En caso que el paciente sea “habitual” se 
le aplicará un descuento del 25%. Por último, si el tipo de cobro es igual a 2 (“tarjeta de crédito”) se le incrementa al anterior 
importe un 20% más; en caso que el cobro sea igual a 1 (“efectivo”) se le realiza un descuento del 10% sobre el anterior importe.
* El importe total de las atenciones de farmacia se calcula a partir del importe total de los medicamentos vendidos. Luego se le 
realiza el descuento del cupón de descuento cuyo importe está especificado. Por último, si el tipo de cobro es igual a 2 (“tarjeta de 
crédito”) se leincrementa al anterior importe un 30% más; en caso que el cobro sea igual a 1 (“efectivo”) se le realiza un descuento 
del 5% sobre elanterior importe.

Con lo expuesto anteriormente, usted deberá implementar:

* Todas las clases del modelo presentado.
* Los siguientes requerimientos de métodos:
    * Para las clases Atención, Médica, Farmacia y Paciente implementar su constructor, acceso y modificación y toString.
    * Para la clase Hospital implementar el método addAtención que agrega una atención a la colección.
* Definir e implementar los métodos importeACobrar de las atenciones, que calcule y devuelva el importe a cobrar por la atención de 
acuerdo a los criterios anteriormente especificados.
* En clase Hospital se requiere la implementación de los siguientes métodos:
    * importe_total_atencion_consulta: debe calcular la suma de los importes de las consultas de las atenciones médicas.
    * importe_promedio_atenciones: debe calcular el promedio de los importes a cobrar por aquellas atenciones médicas cuyo importe a 
    cobrar se encuentre entre dos valores recibidos como parámetros.
    * codigo_primera_atencion_habitual: debe retornar el código de la primera atención médica que se haya registrado para un paciente 
    habitual, o 0 si no existe ninguna.
"""
from clases import *


def main():
    hospital = Hospital("Garraham")

    p1 = Paciente("Juan Perez", 1, True)
    p2 = Paciente("Ana Gomez", 2, False)
    p3 = Paciente("Luis Rodriguez", 3, True)
    p4 = Paciente("Marta Sanchez", 1, False)
    p5 = Paciente("Carlos Fernandez", 2, True)
    p6 = Paciente("Sofia Lopez", 3, False)
    p7 = Paciente("Diego Martinez", 1, True)
    p8 = Paciente("Laura Garcia", 2, False)

    am1 = AtencionMedica(1, 1, p1, 1000)
    am2 = AtencionMedica(2, 2, p2, 2000)
    am3 = AtencionMedica(3, 1, p3, 1500)
    am4 = AtencionMedica(4, 2, p4, 3000)
    am5 = AtencionMedica(5, 1, p5, 2500)
    am6 = AtencionMedica(11, 2, p6, 3500)
    am7 = AtencionMedica(12, 1, p7, 4000)
    am8 = AtencionMedica(13, 2, p8, 4500)

    af1 = AtencionFarmacia(6, 1, 500, 50)
    af2 = AtencionFarmacia(7, 2, 1000, 0)
    af3 = AtencionFarmacia(8, 1, 1500, 100)
    af4 = AtencionFarmacia(9, 2, 2000, 200)
    af5 = AtencionFarmacia(10, 1, 2500, 0)

    hospital.agregar_atencion(am1)
    hospital.agregar_atencion(am2)
    hospital.agregar_atencion(am3)
    hospital.agregar_atencion(am4)
    hospital.agregar_atencion(am5)
    hospital.agregar_atencion(am6)
    hospital.agregar_atencion(am7)
    hospital.agregar_atencion(am8)
    hospital.agregar_atencion(af1)
    hospital.agregar_atencion(af2)
    hospital.agregar_atencion(af3)
    hospital.agregar_atencion(af4)
    hospital.agregar_atencion(af5)

    for atencion in hospital.atenciones:
        print(atencion)

    importeTotalAM = hospital.importe_total_atencion_consulta()
    promedioAM = hospital.importe_promedio_atenciones(2000, 4000)
    codigoPrimeraAtencionHabitual = hospital.codigo_primera_atencion_habitual()

    print(f"\nImporte total de atenciones médicas: {importeTotalAM}")
    print(f"Promedio de atenciones médicas entre 2000 y 4000: {promedioAM}")
    print(f"Código de la primera atención médica para un paciente habitual: {codigoPrimeraAtencionHabitual}")

if __name__ == "__main__":
    main()