
import random

# dic = {
#     'chave': 'valor'
# }
# print(dic['chave'])

# dic['nova_chave'] = 'novo valor'
# print(dic)

# dic['chave'] = 'valor 2'
# print(dic)

'''--------------------------------------------------'''

# dic = {
#     'Oi': 'Olá',
#     'Tchau': 'flw'
# }
# resposta = input('Diga Oi ou Tchau: ')
# print(dic[resposta])

'''--------------------------------------------------'''

# dic = {
#     'Oi': ['Olá', 'Salve', 'Saudações', 'Eaí'],
#     'Tchau': ['flw', 'vlw', 'hasta la vista', 'boa', 'tmj']
# }
# resposta = input('Diga Oi ou Tchau: ')
# print(random.choice(dic[resposta]))

'''--------------------------------------------------'''

# lados = int(input('Diga o número de lados do seu polígono: '))
# if (lados == 3):
#     print('Triângulo')
# elif (lados == 4):
#     print('Quadrado')
# elif (lados == 5):
#     print('Pentágono')
# if (lados == 6):
#     print('Hexágono')


# formas = {
#     '3': 'Triângulo',
#     '4': 'Quadrado',
#     '5': 'Pentágono',
#     '6': 'Hexágono'
# }
# lados = input('Diga o número de lados do seu polígono: ')
# print(formas[lados])

'''--------------------------------------------------'''

#declare um dicionário vazio
#crie a chave pares
#crie a chave ímpares
#associe a ambas listas vazias
#preencha com pares e ímpares até 100

# dic = {}
# dic['pares'] = [i for i in range(0,100,2)]
# dic['impares'] = [i for i in range(1,100,2)]
# print(dic)

# dic['pares'] = list(range(0,100,2))
# dic['impares'] = list(range(1,100,2))
# print(dic)

# dic['pares'] = []
# dic['impares'] = []

# for i in range(100):
#     if (i % 2 == 0):
#         dic['pares'].append(i)
#     else:
#         dic['impares'].append(i)
# print(dic)

'''--------------------------------------------------'''

numeros = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9
}

frase = 'Meu número é um dois três quatro cinco seis sete oito nove'
frase = frase.lower()
frase = frase.split(' ')
print(frase)

for i in range(len(frase)):
    if (frase[i] in numeros.keys()):
        frase[i] = str(numeros[frase[i]])

frase = ' '.join(frase)
print(frase)
