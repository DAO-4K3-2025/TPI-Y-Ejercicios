from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(codigo, titulo, autor, precio_base)
        self.tipo = 3
        self.origen = origen

    def calcular_costo_mantenimiento(self):
        costoBase = 50
        if self.origen == "nacional":
            return costoBase
        elif self.origen == "importada":
            return costoBase * 1.2