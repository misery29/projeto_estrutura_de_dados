class Tipo:
    def __init__(self):
        self.tipo = ['Canino', 'Felino']

    def append_tipo(self, tipo):
        self.tipo.append(tipo)


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


class Sistema(Tipo):
    def __init__(self):
        super().__init__()
        self.pessoas = []
        self.animais = []

    def adiciona_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    def adiciona_animal(self, animal):
        self.animais.append(animal)
        print("Animal cadastrado com sucesso!")

    def exibir_animais(self):
        if self.animais:
            print("Animais cadastrados:")
            for animal in self.animais:
                self.exibir_atributo(animal, "tipo")
                self.exibir_atributo(animal, "idade")
                self.exibir_atributo(animal, "cor")
                self.exibir_atributo(animal, "porte")
                self.exibir_atributo(animal, "particularidade")
                print("-" * 20)
        else:
            print("Nenhum animal cadastrado.")

    def exibir_pessoas(self):
        if self.pessoas:
            print("Pessoas cadastradas:")
            for pessoa in self.pessoas:
                self.exibir_atributo(pessoa, "nome")
                self.exibir_atributo(pessoa, "contato")
                self.exibir_atributo(pessoa, "especie_interesse")
                self.exibir_atributo(pessoa, "preferencia")
                print("-" * 20)
        else:
            print("Nenhuma pessoa cadastrada.")

    def ordena_animais(self, atributo):
        self.animais.sort(key=lambda x: getattr(x, atributo.lower()) if getattr(x, atributo.lower()) is not None else '')
    # Ordena os animais de acordo com um atributo
    def pesquisa_binaria(self, atributo, valor):
        self.ordena_animais(atributo)
        resultados = []  # lista para armazenar os animais encontrados
        inicio = 0
        fim = len(self.animais) - 1

        # Converter o valor para minúsculas
        valor = valor.lower()

        while inicio <= fim:
            meio = (inicio + fim) // 2
            valor_animal = getattr(self.animais[meio], atributo).lower()

            if valor_animal == valor:
                resultados.append(self.animais[meio])
                # Verificar animais com o mesmo valor à esquerda do meio
                i = meio - 1
                while i >= 0 and getattr(self.animais[i], atributo).lower() == valor:
                    resultados.append(self.animais[i])
                    i -= 1
                # Verificar animais com o mesmo valor à direita do meio
                i = meio + 1
                while i <= fim and getattr(self.animais[i], atributo).lower() == valor:
                    resultados.append(self.animais[i])
                    i += 1
                break
            elif valor_animal < valor:
                inicio = meio + 1
            else:
                fim = meio - 1
        self.exibir_resultados_pesquisa(resultados)
        return resultados
    def exibir_resultados_pesquisa(self, resultados):
        if resultados:
            print("Animais encontrados:")
            for animal in resultados:
                self.exibir_atributo(animal, "tipo")
                self.exibir_atributo(animal, "idade")
                self.exibir_atributo(animal, "cor")
                self.exibir_atributo(animal, "porte")
                self.exibir_atributo(animal, "particularidade")
                print("-" * 20)
        else:
            print("Nenhum animal encontrado com o valor especificado.")

    def exibir_atributo(self, objeto, atributo):
        valor = getattr(objeto, atributo, None)
        if valor is not None:
            print(f"{atributo.capitalize()}: {valor}")
        else:
            print(f"{atributo.capitalize()}: N/A")

    def relatorio_cruzamento(self):
        print("Relatório de Cruzamento de Interesses:\n")

        for pessoa in self.pessoas:
            print(f"Pessoa: {pessoa.nome}")
            interesses = pessoa.especie_interesse.split(",")
            encontrados = False

            for interesse in interesses:
                interesse = interesse.strip()
                resultados = self.pesquisa_binaria("tipo", interesse)

                if resultados:
                    encontrados = True

                    for animal in resultados:
                        print("--------------------")
                        print(f"Animais encontrados para o tipo '{interesse}':")
                        self.exibir_atributo(animal, "tipo")
                        self.exibir_atributo(animal, "idade")
                        self.exibir_atributo(animal, "cor")
                        self.exibir_atributo(animal, "porte")
                        self.exibir_atributo(animal, "particularidade")
                        print("-" * 20)

            if not encontrados:
                print(f"Nenhum animal encontrado para os tipos de interesse de {pessoa.nome}.")

            print("--------------------")
