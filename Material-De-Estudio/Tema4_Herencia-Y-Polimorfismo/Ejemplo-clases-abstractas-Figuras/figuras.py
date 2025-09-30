from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
	def __init__(self, nombre):
		self.nombre = nombre

	@abstractmethod
	def superficie(self):
		pass

	@abstractmethod
	def perimetro(self):
		pass

	def obtener_nombre(self):
		return self.nombre

class Circulo(FiguraGeometrica):
	def __init__(self, radio):
		super().__init__("Círculo")
		self.radio = radio

	def superficie(self):
		return math.pi * self.radio ** 2

	def perimetro(self):
		return 2 * math.pi * self.radio

class Triangulo(FiguraGeometrica):
	def __init__(self, lado1, lado2, lado3):
		super().__init__("Triángulo")
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def superficie(self):
		s = (self.lado1 + self.lado2 + self.lado3) / 2
		return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

	def perimetro(self):
		return self.lado1 + self.lado2 + self.lado3

class Rectangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		super().__init__("Rectángulo")
		self.base = base
		self.altura = altura

	def superficie(self):
		return self.base * self.altura

	def perimetro(self):
		return 2 * (self.base + self.altura)

# class Trapecio(FiguraGeometrica):
# 	def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
# 		super().__init__("Trapecio")
# 		self.base_mayor = base_mayor
# 		self.base_menor = base_menor
# 		self.altura = altura
# 		self.lado1 = lado1
# 		self.lado2 = lado2

# 	def superficie(self):
# 		return ((self.base_mayor + self.base_menor) * self.altura) / 2

# 	def perimetro(self):
# 		return self.base_mayor + self.base_menor + self.lado1 + self.lado2

# Ejemplos de uso:
if __name__ == "__main__":
	figuras = [
		Circulo(5),
		Triangulo(3, 4, 5),
		Rectangulo(2, 6),
		# Trapecio(8, 4, 3, 5, 5)
	]
	for figura in figuras:
		print(f"{figura.obtener_nombre()} - Superficie: {figura.superficie():.2f}, Perímetro: {figura.perimetro():.2f}")
