
# def hello_world(lista):
#     for numero in lista:
#         print(numero)
#     a = 100
#     b = True
#     return "Hello World!"
#
# lista = [1, 2, 3, 4, 5]
# lista2 = lista
# lista2[0] = 900
# print(lista)

# def printa_lista(numeros):
#     print(numeros)
#     for num in lista:
#         print(num)
#     return
#
# lista = [1,2,3,4,5]
# printa_lista([7, 8, 3, 4, 9])

'''--------------------------------------------------'''

# lista = [0,1,0,0,1,0,1,0,0,1]
# lista2 = [0,0,1]
#
# qtd = 0
# for i in range(len(lista)):
#     for j in range(len(lista2)):
#         if (lista[i + j] != lista2[j]):
#             break
#         elif (j == len(lista2) - 1):
#             qtd += 1
# print(qtd)

# lista = [0,0,1,0,0,1,0,0]
# lista2 = [0,0,1,0,0]
#
# qtd = 0
# j = 0
# for i in range(len(lista) - len(lista2)):
#     print(lista[i],lista2[j])
#     if (lista[i] == lista2[j]):
#         j += 1
#     if (j == len(lista2) - 1):
#         qtd += 1
#         j = 0
# print(qtd)

lista = [0,1,0,0,1,0]
listinha = [0,1,0]

qtd = 0
print(len(lista) - len(listinha))
for i in range(len(lista) - len(listinha) + 1): # es "+ 1" que faz a diferença
    print(f'i: {i}')
    print(f'lista[i]: {lista[i]}')
    for j in range(len(listinha)):
        print(f'j: {j}')
        if (lista[i + j] != listinha[j]):
            print('break')
            break
    if (j == len(listinha) - 1):
        qtd += 1
print(f'qtd: {qtd}')
