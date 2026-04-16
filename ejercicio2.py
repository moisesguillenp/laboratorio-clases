#Crea una clase "Coche" con propiedades para la marca, el modelo y el año de fabricación, y un método para obtener el número de años que ha pasado desde que se fabricó el coche.
import datetime
class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def año_antiguedad (self):
        año_actual = datetime.now().year
        return año_actual - self.año