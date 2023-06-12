from mainClass import *
from mainDefs import *

# Função para executar os testes
def testes():
    sistema = Sistema()

    # Cenário 1: Cadastrar animais e pessoas
    animal1 = Animal("Canino", 3, "Marrom", "Pequeno", "Late muito")
    animal2 = Animal("Felino", 5, "Preto", "Médio", "Gosta de brincar")
    sistema.adiciona_animal(animal1)
    sistema.adiciona_animal(animal2)

    pessoa1 = Pessoa("João", "123456789", "Felino", "Gosta de animais brincalhões")
    pessoa2 = Pessoa("Maria", "987654321", "Canino", "Prefere animais de pequeno porte")
    sistema.adiciona_pessoa(pessoa1)
    sistema.adiciona_pessoa(pessoa2)

testes()