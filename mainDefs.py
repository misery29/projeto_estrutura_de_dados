from mainClass import *


def menu(sistema):
    while True:
        print("""Selecione uma opção:
        1. Cadastrar Animal
        2. Cadastrar Pessoa
        3. Cadastrar Tipo
        4. Pesquisar Animais
        5. Relatório Cruzamento
        6. Sair""")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("Você selecionou a opção 1.")
            for p, t in enumerate(sistema.tipo):
                print(p, "-", t)
            tipo =  int(input("Informe o tipo: "))
            idade = int(input("Informe a idade: "))
            cor = input("Informe a cor: ")
            porte = input("Informe o porte: ")
            particularidade = input("Informe a particularidade: ")
            animal = Animal(sistema.tipo[tipo], idade, cor, porte, particularidade)
            sistema.adiciona_animal(animal)
            print("Animal cadastrado com sucesso.")

        elif escolha == "2":
            print("Você selecionou a opção 2.")
            nome = input("Informe o nome: ")
            contato = input("Informe o número: ")
            especie_interesse = input("Informe a espécie interessada: ")
            preferencia = input("Informe a preferência: ")
            pessoa = Pessoa(nome, contato, especie_interesse, preferencia)
            sistema.adiciona_pessoa(pessoa)
            print("Pessoa cadastrada com sucesso.")

        elif escolha == "3":
            print("Você selecionou a opção 3.")
            tipo = input("Informe o tipo do animal: ")
            sistema.append_tipo(tipo)
            print("Tipo cadastrado com sucesso.")

        elif escolha == "4":
            print("Você selecionou a opção 4.")
            atributo = input("Informe o atributo para pesquisa: ")
            valor = input("Informe o valor para pesquisa: ")
            sistema.pesquisa_binaria(atributo, valor)

        elif escolha == "5":
            print("Você selecionou a opção 5.")
            sistema.relatorio_cruzamento()

        elif escolha == "6":
            print("Você selecionou a opção 6. Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")
