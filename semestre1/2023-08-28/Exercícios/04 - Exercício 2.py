'''
2. Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
'''

ano = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - ano
if (idade >= 16):
    print('Você poderá votar este ano.')
else:
    print('Você não poderá votar este ano.')
