animais_disponiveis = [
    {"nome": "Bolinha", "espécie": "cachorro", "raça": "vira-lata", "idade": 2, "sexo": "macho", "temperamento": "brincalhão"},
    {"nome": "Luna", "espécie": "gato", "raça": "persa", "idade": 3, "sexo": "fêmea", "temperamento": "independente"},
    {"nome": "Mel", "espécie": "gato", "raça": "siames", "idade": 1, "sexo": "fêmea", "temperamento": "calmo"},
    {"nome": "Rex", "espécie": "cachorro", "raça": "pastor-alemao", "idade": 4, "sexo": "macho", "temperamento": "protetor"},
    {"nome": "Rexudo", "espécie": "cachorro", "raça": "pastor", "idade": 4, "sexo": "macho", "temperamento": "protetor"}
]

def pesquisa_binaria_animais(nome_animal, animais_disponiveis, campo_ordenacao):
    animais_disponiveis_ordenados = sorted(animais_disponiveis, key=lambda x: x[campo_ordenacao])
    inicio = 0
    fim = len(animais_disponiveis_ordenados) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if animais_disponiveis_ordenados[meio][campo_ordenacao] == nome_animal:
            print(animais_disponiveis_ordenados[meio])
            return None
        elif animais_disponiveis_ordenados[meio][campo_ordenacao] < nome_animal:
            inicio = meio + 1
        else:
            fim = meio - 1
            print(animais_disponiveis_ordenados[meio]["nome"])


pesquisa_binaria_animais("2", animais_disponiveis, "idade")