# listaPar = []
# listaImpar = []
# for i in range(1, 20):
#     if (i % 2 == 0):
#         listaPar.append(i)
#     else:
#         listaImpar.append(i)
#
# print(f'Pares: {listaPar}')
# print(f'Ímpares: {listaImpar}')

# listaPar = []
# listaImpar = []
# for i in range(0, 20, 2):
#     listaPar.append(i)
#
# for i in range(1, 20, 2):
#     listaImpar.append(i)
#
# print(f'Pares: {listaPar}')
# print(f'Ímpares: {listaImpar}')

'''--------------------------------------------------'''

# lista = []
# for i in range(10):
#     inputText = f'Digite a {i+1}ª nota: '
#     nota = input(inputText)
#     while (not nota.isnumeric()):
#         print('Digite um valor válido!')
#         nota = input(inputText)
#     nota = int(nota)
#
#     lista.append(nota)
#
# soma = 0
# qtd_acima_5 = 0
# qtd_abaixo_5 = 0
# for i in lista:
#     soma += i
#     if (i > 5):
#         qtd_acima_5 += 1
#     else:
#         qtd_abaixo_5 += 1
# print(f'Média das notas: {len(lista)}')
# print(f'Quantidade de nota acima de 5: {qtd_acima_5}')
# print(f'Quantidade de nota abaixo de 5: {qtd_abaixo_5}')

'''--------------------------------------------------'''

listaNome = ['Celta', 'Corsa', 'Ferrari']
listaValor = [10, 50, 30]

maior = listaValor[0]
index_maior = listaNome[0]
for i in range(len(listaValor)):
    if (listaValor[i] > maior):
        maior = listaValor[i]
        index_maior = i
print(listaNome[index_maior])