from mainClass import *
from mainDefs import *

sistema = Sistema()

animal1 = Animal("Felino", 3, "Rajado", "Pequeno", "Mija demais")
animal2 = Animal("Canino", 8, "Branci", "Grande", "Late pouco")
animal3 = Animal("Canino", 3, "Marrom", "Pequeno", "Late muito")
animal4 = Animal("Felino", 5, "Preto", "Médio", "Gosta de brincar")
sistema.adiciona_animal(animal1)
sistema.adiciona_animal(animal2)
sistema.adiciona_animal(animal3)
sistema.adiciona_animal(animal4)


pessoa1 = Pessoa("João", "123456789", "Felino", "Gosta de animais brincalhões")
pessoa2 = Pessoa("Maria", "987654321", "Canino", "Prefere animais de pequeno porte")
sistema.adiciona_pessoa(pessoa1)
sistema.adiciona_pessoa(pessoa2)


menu(sistema)
