#Crea una clase "Tienda" con propiedades para el nombre de la tienda y una lista de productos disponibles, 
#y métodos para añadir o eliminar productos de la lista y para obtener la lista completa de productos.
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def listar_productos(self):
        return self.productos