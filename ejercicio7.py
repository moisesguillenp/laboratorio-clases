#Crea una clase "Banco" con propiedades para el nombre del banco y la tasa de interés,
#y métodos para calcular el interés que se obtendría en una cantidad determinada de dinero y el tiempo que se tardaría en duplicar esa cantidad.
class Banco:
    def __init__(self, nombre, tasa_interes):
        self.nombre = nombre
        self.tasa_interes = tasa_interes  # en porcentaje

    def calcular_interes(self, capital, tiempo):
        return capital * (self.tasa_interes / 100) * tiempo

    def tiempo_para_duplicar(self):
        # fórmula aproximada: 72 / tasa (regla del 72)
        return 72 / self.tasa_interes