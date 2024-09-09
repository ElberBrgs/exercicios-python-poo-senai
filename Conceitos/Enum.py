from os import system
from enum import Enum

system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self,nome:str,idade:int,sexo:Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}") # O .value trás o valor (no caso string) do Enum.
    
#Instanciando classe Pessoa.
pessoa_um = Pessoa("Duquinha Pressão",24,Sexo.MASCULINO)
print(pessoa_um)