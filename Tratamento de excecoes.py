from os import system
system("cls || clear")

#CRIANDO PRÓPRIA EXCEÇÃO
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self,numero_conta:int,agencia:int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        #Pré-determina valor no construtor.
        self._saldo = 0 #Atributo privado.
    
    @property
    def saldo(self):
        return self._saldo
    
    
    def __verificar_sacar(self,valor):#Método privado: "Um método privado serve de apoio para um método público."
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.") #Lançando uma exceção.
        
    def sacar(self,valor):
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"

        self._saldo -= valor
        return self._saldo
    
    def __verificar_depositar(self,valor):
        if valor < 0:
            raise ValorNegativoError("Valor inválido.") #Lançando uma exceção.
    
    def depositar(self,valor):
        try: 
            self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"
        
        self._saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar classes.
conta_corrente_um = ContaCorrente(555,333)
conta_poupanca_um = ContaPoupanca(666,222)

print(conta_corrente_um.saldo) 
print(conta_corrente_um.sacar(200))
print(conta_corrente_um.saldo)
print(conta_corrente_um.depositar(-200))