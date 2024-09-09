from abc import ABC,abstractmethod
from os import system

system("cls || clear")

#ATUALIZAR REGRA DE NEGOCIO: VALIDAR VALOR NEGATIVO NO SALÁRIO

class SalarioNegativoError(Exception):
    pass

class Endereco:
    def __init__(self,logradouro:str,numero:str,cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nCidade: {self.cidade}"
            )
    
#Classe abstrata   
class Funcionario(ABC):
    def __init__(self,nome:str,email:str,endereco:Endereco) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def __verificar_salario_negativo(self,valor):
        if valor < 0:
            raise SalarioNegativoError("Salário inválido.")
    
    @abstractmethod
    def salario_final(self,valor)->float:
        pass

    def __str__(self) -> str:
        return (
                f"\n---Funcionário---"
                f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalário: R${self.salario_final()}"
                f"\n---Endereço---{self.endereco}")
    
#    
class Motoboy(Funcionario):
    def __init__(self, nome: str,cnh: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, email, endereco)
        self.cnh = cnh

    def salario_final(self,valor) -> float:
        
        try: 
            self.__verificar_salario_negativo(valor)
        except SalarioNegativoError as error:
            return f"Erro: {error}"
        

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n------------"
            f"\nCNH: {self.cnh}")
    
#Instanciando classes
funcionario_um = Motoboy("Joao","6548213","Jaozin@email.com",
                             Endereco("Rua Via","201","Salvador"))

print(funcionario_um)