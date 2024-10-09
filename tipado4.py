class termostato:
    def __int__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial

    def aumentar_temperatura(self, grados):
        self.temperatura += grados 

    def disminuir_temperatura(self, grados):
        self.temperatura -= grados 

    def mostrar_temperatura(self):
        print(f"la temperatura actual es {self.temperatura}°c.")