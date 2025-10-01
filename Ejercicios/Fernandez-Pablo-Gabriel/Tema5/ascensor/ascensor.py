""" Un ascensor posee una capacidad máxima de n personas y está
    instalado en un edificio cuyos pisos se encuentran numerados. Se
    necesita desarrollar una clase Ascensor que represente el
    funcionamiento del mismo y que posea métodos para:

*   Desplazarse a un piso determinado
*   Subir personas
*   Bajar personas
*   Informar el piso donde se encuentra y la cantidad de personas
    que hay adentro """

class Ascensor:
    def __init__(self, pisoInferior, pisoSuperior, capMaxima):
        if capMaxima <= 0:
            raise ValueError("La capacidad mínima debe ser mayor a 0...")
        else:
            self.capMaxima = capMaxima
        self.validar_rango_pisos(pisoInferior, pisoSuperior)
        self._pisoInferior = pisoInferior
        self._pisoSuperior = pisoSuperior
        self.personas = 0
        self.piso_actual = 0

    def validar_rango_pisos(self, pisoInferior, pisoSuperior):
        if pisoInferior >= pisoSuperior:
            raise ValueError("El piso inferior no puede ser mayor al superior...")
        elif pisoInferior > 0:
            raise ValueError("El piso inferior no puede ser mayor a 0...")
        elif pisoSuperior < 0:
            raise ValueError("El piso superior no puede ser menor a 0...")
    
    def ir_a_piso(self, piso):
        if self._pisoInferior <= piso <= self._pisoSuperior:
            self.piso_actual = piso
            return True
        else:
            return False
            # raise ValueError("El piso inicial esta fuera del rango definido...")

    def subir(self, nuevasPer):
        total = self.personas + nuevasPer
        if nuevasPer <= 0:
            return -1

        if total > self.capMaxima:
            # raise ValueError("Se excedió el nùmero de personas permitidas...")
            personasQueSuben = self.capMaxima - self.personas
            self.personas = self.capMaxima
            return personasQueSuben
            #return self.capMaxima
        else:
            self.personas = total
            return nuevasPer


    def bajar(self, menosPer):
        if menosPer > self.personas:
            aux = self.personas
            self.personas = 0
            return aux
        elif menosPer <= 0:
            return -1
        else:
            self.personas -= menosPer
            return menosPer

    
    def __str__(self):
        return f"El ascensor se encuentra en el piso {self.piso_actual} y con {self.personas} personas"
        