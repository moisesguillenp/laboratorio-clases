import datetime
class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def año_antiguedad (self):
        año_actual = datetime.date.today().year
        return año_actual - self.año

coche1 = coche("toyota", "corolla", 2018)
print(coche1.año_antiguedad())