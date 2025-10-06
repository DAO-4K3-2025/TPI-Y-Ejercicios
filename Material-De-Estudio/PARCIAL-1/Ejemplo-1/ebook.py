from material import Material

class Ebook(Material):
    def __init__(self, codigo, titulo, autor, precio_base, valor_venta):
        super().__init__(codigo, titulo, autor, precio_base)
        self.tipo = 2
        self.valor_venta = valor_venta

    def calcular_costo_mantenimiento(self):
        return self.valor_venta * 0.05
    
