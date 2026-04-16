#Crea una clase "Círculo" con propiedades para el radio y el diámetro, y métodos para calcular el área y la circunferencia del círculo.
import math
class circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = radio * 2

    def calcular_area(self):
        return math.pi *self.radio ** 2
    
    def calcular_circunferencia(self):
        return 2 *math.pi* self.radio