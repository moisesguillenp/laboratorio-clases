#Crea una clase "Estudiante" con propiedades para el nombre, la edad y la carrera, y 
#métodos para obtener y establecer estas propiedades, así como un método para calcular la nota media de un conjunto de exámenes.
import math
class estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    def obtener_nombre(self):
        return self.nombre
    def colocar_nombre(self, nombre):
        self.nomre = nombre
    def calcular_promedio(self, notas):
        return sum(notas) / len(sum)