class CuentaBancaria: 
     def __int__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo 
        
     def depositar(self, cantidad):
         self.saldo += cantidad
         
     def retira(self, cantidad):
         if cantidad <= self.saldo:
             self.saldo -= cantidad 
         else:
             print("saldo insuficiente")
               
         def mostrar_saldo(self):
             print(f" el saldo de {self.titular} es {self.saldo}.")