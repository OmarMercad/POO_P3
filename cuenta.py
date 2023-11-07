class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print('Construyendo el Objeto...{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extracto(self):
        print("saldo {} del titular {}  ".format(self.saldo,self.titular))
    
    def depositar(self,valor):
        self.saldo += valor
        
    def retirar (self,valor):
        if(valor<= self.saldo):
            self.saldo -= valor
        else:
            print("No tiene suficiente saldo")
            