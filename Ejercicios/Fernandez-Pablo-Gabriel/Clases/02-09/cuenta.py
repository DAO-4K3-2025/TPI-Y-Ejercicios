class Cuenta:

    def __init__(self,titular, monto=0):
        self.titular = titular
        self.monto = monto


    def __str__(self):
        return "Titular: (" + str(self.titular) + ") | Monto: " + str(self.monto)
    
    def saldo(self):
        return self.monto
    
    def depositar(self, monto):
        if monto > 0:
            self.monto += monto

    def extraer(self, monto):
        if monto < self.monto:
            self.monto = self.monto - monto
            return "Monto extraido!"
        else:
            return "Excede al valor de la cuenta..."