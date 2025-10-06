from material import Material
class Libro(Material):
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self.tipo = 1
        self.dias_prestados = dias_prestados
    
    def calcular_costo_mantenimiento(self):
        cociente = self.dias_prestados // 30
        return 100 + (100 * cociente)