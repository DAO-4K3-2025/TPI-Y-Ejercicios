""" Leer todo el archivo de empleados. El mismo posee los siguientes datos:

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
from empleado import *
import csv

def leer_csv(arch):
    with open(arch, "r") as csv_arch:
        listaEmpleados = csv.reader(csv_arch, delimiter=";")
        return list(listaEmpleados)
    
# Asumo que en la columna tipo solo hay 1, 2 y 3
def instanciar_empleados(empleados):
    listaEmpleados = []
    for emp in empleados:
        if emp[0] == '1':
            listaEmpleados.append(Obrero(emp[1], emp[2], emp[3], float(emp[4]), int(emp[5])))
        elif emp[0] == '2':
            listaEmpleados.append(Administrativo(emp[1], emp[2], emp[3], float(emp[4]), emp[5]))
        else:
            listaEmpleados.append(Vendedor(emp[1], emp[2], emp[3], float(emp[4]), float(emp[5])))
    
    """ for emp in listaEmpleados:
        print(emp) """

    return listaEmpleados

# Calcular el total a pagar de sueldos
def calcular_total_sueldos(listaEmpleados):
    totalSueldos = 0
    for emp in listaEmpleados:
        totalSueldos += emp.calcular_sueldo()
    
    return round(totalSueldos, 2)

# Contar los empleados por tipo (tres totales)
def contar_empleados_por_tipo(listaEmpleados):
    empleadosTipos = [0, 0, 0]
    for emp in listaEmpleados:
        if emp.devolver_tipo() == "Obrero":
            empleadosTipos[0] += 1
        elif emp.devolver_tipo() == "Administrativo":
            empleadosTipos[1] += 1
        else:
            empleadosTipos[2] += 1
    
    return empleadosTipos

# Buscar un empleado por legajo y mostrar el sueldo a pagar 
def devolver_sueldo_empleado(legajo, listaEmpleados):
    for emp in listaEmpleados:
        if emp.legajo == legajo:
            return emp.calcular_sueldo()
    return -1


def main():
    arch = "empleados.csv"
    cadenaEmpleados = leer_csv(arch)
    listaEmpleados = instanciar_empleados(cadenaEmpleados)

    print("*** EMPLEADOS ***")
    print(f"- El total a pagar de sueldos es de: ${calcular_total_sueldos(listaEmpleados)}")
    empleadosTipos = contar_empleados_por_tipo(listaEmpleados)
    print(f"- Se contaron los siguientes empleados por tipo:\
            \n  - Obrero: {empleadosTipos[0]}\
            \n  - Administrativo: {empleadosTipos[1]}\
            \n  - Vendedor: {empleadosTipos[2]}\
            \n  - Total: {len(listaEmpleados)}")
    
    legajoBuscado = input("- Ingrese el legajo de un empleado para obtener su sueldo a pagar: ")
    sueldoObtenido = devolver_sueldo_empleado(legajoBuscado, listaEmpleados)
    if sueldoObtenido != -1:
        print(f"+ El sueldo a pagar al empleado {legajoBuscado} es: ${str(sueldoObtenido)}")
    else:
        print("+ No se ha encontrado el empleado...")

    
    
    

if __name__ == "__main__":
    main()