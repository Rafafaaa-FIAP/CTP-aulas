'''
Faça uma função que recebe uma lista contendo nomes de pessoas, pergunte ao usuário quantas pessoas ele quer cadastrar e cadastre-as
'''

def checkNumber(inputText):
    qtd = input(inputText)
    while (not qtd.isnumeric()):
        print('Digite um número!')
        qtd = input(inputText)
    return int(qtd)

def cadastrarPessoa(pessoas):
    qtd = checkNumber('Quantas pessoas deseja cadastrar? ')
    for i in range(qtd):
        pessoas.append(input(f'Digite o nome da { i + 1 }ª pessoa: '))
    return pessoas

people = []
print(people)
people = cadastrarPessoa(people)
print(people)
people = cadastrarPessoa(people)
print(people)
