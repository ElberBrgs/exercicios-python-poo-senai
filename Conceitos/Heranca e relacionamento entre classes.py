from abc import ABC,abstractmethod
from os import system

system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
    
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
                )

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__()
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self)->float:
        pass

    def __str__(self) -> str:
        return (
            f"\n---Funcionario---"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n---Endereco---{self.endereco}"
            f"\nSalario: R${self.salario_final()}"
                )

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
                )

    def salario_final(self) -> float:
        return 2000.0

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCRM: {self.crm}"
                )

#Instanciando classes.

engenheiro_1 = Engenheiro("Joao","71956723987","Joaozao@email.com",
                          Endereco("Rua Via Alameda","500","Primeira etapa","41320687","Salvador"),"321572")

print(engenheiro_1)        

medico_1 = Medico("Maria","71956723987","Mariazinha@email.com",
                          Endereco("Rua Via Alameda","526","Segunda etapa","41320687","Salvador"),"BA371377")

print(medico_1)
