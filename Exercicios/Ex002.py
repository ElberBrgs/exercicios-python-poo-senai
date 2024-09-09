from os import system
from enum import Enum

system("cls || clear")

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Funcionario:
    def __init__(self,id:int,nome:str,idade:int,salario:float,setor:Setor,sexo:Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        return(
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSalário: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            )
    
funcionario_um = Funcionario(762,"Lil Duca Pressure",23,5000,Setor.FINANCEIRO,Sexo.MASCULINO)
funcionario_dois = Funcionario(157,"Mary Jane",21,3000,Setor.RECURSOS_HUMANOS,Sexo.FEMININO)

print(funcionario_um)
print(funcionario_dois)