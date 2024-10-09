class Libro:
    def __init__(self,titulo,autor):
        self.titulo= titulo
        self.autor= autor
        self.disponible= True #Mayuscula

    def prestar(self):
        if self.disponible:
            self.dispoible= False
            print(f"El libro{self.tituolo} ha sido prestado")
        else:
            print(f"El libro {self.titulo} no se encuentra disponible")
    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto")
    def mostrarestado(self):
        estado= "disponible"if self.disponible else "prestado"
        print(f"El libro {self.titulo}esta {estado}")

