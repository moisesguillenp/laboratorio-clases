#Crea una clase "Empleado" con propiedades para el nombre, la edad, el salario y el cargo,
#y métodos para obtener y establecer estas propiedades, así como un método para calcular el salario anual.
class empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo
    
    def obtener_salario(self):
        return self.salario
    
    def colocar_salario(self, salario):
        self.salario = salario
        
    def salario_anual(self):
        return self.salario * 12