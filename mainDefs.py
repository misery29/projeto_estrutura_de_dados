from mainClass import *

def menu(sistema):
    while True:
        print("""Selecione uma opção:
        1. Cadastrar Animal
        2. Cadastrar Pessoa
        3. Cadastrar Tipo
        4. Sair""")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("Você selecionou a opção 1.")
            tipo =  input("Informe o tipo: ")
            idade = int(input("Informe a idade: "))
            cor = input("Informe a cor: ")
            porte = input("Informe o porte: ")
            particularidade = input("Informe a particularidade: ")
            animal = Animal(tipo, idade, cor, porte, particularidade)
            sistema.adiciona_animal(animal)

        elif escolha == "2":
            print("Você selecionou a opção 2.")
            nome = input("Informe o nome: ")
            contato = input("Informe o número: ")
            especie_interesse = input("Informe a especie interessada: ")
            preferencia = input("Informe a preferência: ")
            pessoa = Pessoa(nome, contato, especie_interesse, preferencia)
            sistema.adiciona_pessoa(pessoa)

        elif escolha == "3":
            print("Você selecionou a opção 3.")

        elif escolha == "4":
            sistema.exibir_animal()
            sistema.exibir_pessoa()
            print("Saindo...")
            
        else:
            print("Opção inválida. Por favor, tente novamente.")

