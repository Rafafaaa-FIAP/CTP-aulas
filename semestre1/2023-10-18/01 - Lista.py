
# precos = [4,2,7,5,6,1]
# indice_maior = 0
# maior = precos[indice_maior]
# for i in range(len(precos)):
#     candidato = precos[i]
#     if (candidato > maior):
#         maior = candidato
#         indice_maior = i
# print(precos[indice_maior])

# precos = [4, 2, 7, 5, 6, 1]
# carros = ['uno', 'up', 'kombi', 'celta', 'mobi', 'kwid', 'gol']
# indice_maior = 0
# maior = precos[indice_maior]
# for i in range(len(precos)):
#     candidato = precos[i]
#     print(f'Vou testar se {candidato} > {maior}')
#     if (candidato > maior):
#         print(f'Vou trocar {maior} por {candidato}')
#         maior = candidato
#         indice_maior = i
# print(f'O carro mais caro é o {carros[indice_maior]} e vale R${precos[indice_maior]},00')

'''--------------------------------------------------'''

'''
1) Dê as opções de carro e obrigue o usuário a escolher uma delas.
2) Encontre o local do carro na lista.
3) Traga todas as informações sobre o carro.
'''

# carros = ['uno', 'up', 'kombi', 'celta', 'mobi', 'kwid', 'gol']
# precos = [4, 2, 7, 5, 6, 1]
# potencias = [10, 20, 30, 40, 50, 60, 70]
# anos = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
#
# inputText = 'Nossos carros são:'
# for i in range(len(precos)):
#     inputText += f'\n - {carros[i]}'
# inputText += '\nEscolha um carro: '
#
# carro_selecionado = input(inputText)
# while (carro_selecionado not in carros):
#     print('Opção inválida!')
#     carro_selecionado = input(inputText)
#
# indice = 0
# for i in range(len(carros)):
#     if (carros[i] == carro_selecionado):
#         indice = i
#         break
#
# print(f'\nModelo: {carro_selecionado}\nPreço: R$ {precos[indice]}\nPotência: {potencias[indice]}\nAno: {anos[indice]}')

'''--------------------------------------------------'''

import sys
print(sys.getsizeof([i for i in range(100000)]))
print(sys.getsizeof(range(100000)))
