class CarritoDeCompras:
    def __init__(self):
        self.productos=[]
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_productos(self,producto):
        if producto in self.productos:
            self.productos.remove(producto)
        
    def mostrar_productos(self):
        if self.productos:
            print("productos en el carrito:",",".join(self.productos))

        else:
            print ("el carrito esta vacio.")




