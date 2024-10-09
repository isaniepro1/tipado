class Cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad  
        self.nivel_actual = 0  

    def llenar(self):
        self.nivel_actual = self.capacidad
        print("La cafetera ha sido llenada.")

    def servir_taza(self):
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            print("Se ha servido una taza de café.")
        else:
            print("No hay café. Llena la cafetera.")

    def mostrar_nivel(self):
        print(f"Nivel actual de café: {self.nivel_actual} tazas.")
