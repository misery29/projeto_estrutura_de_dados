class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

class Pessoa:
    def __init__(self, nome, contato, especie_interesse, preferencia):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse
        self.preferencia = preferencia

class Tipo:
    def __init__(self):
        self.tipo = ['Canino', 'Felino']

    def append_tipo(self, tipo):
        self.tipo.append(tipo)

class Sistema(Tipo):
    def __init__(self):
        super().__init__()
        self.pessoas = []
        self.animais = []

    def adiciona_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
    
    def adiciona_animal(self, animal):
        self.animais.append(animal)

    def exibir_animal(self):
        for animal in self.animais:
            print(animal.tipo, animal.idade, animal.cor, animal.porte, animal.particularidade)

    def exibir_pessoa(self):
        for pessoa in self.pessoas:
            print(pessoa.nome, pessoa.contato, pessoa.especie_interesse, pessoa.preferencia)