
import matplotlib.pyplot as plt

# python -m venv env
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# .\env\Scripts\activate
# python -m pip install --upgrade pip
# clicar no play

def gerar_matriz(linhas, colunas, num = 0):
    matriz =[]

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(num)
        matriz.append(linha)
    print()
    return matriz

def printar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

# xadrez = gerar_matriz(8, 8)

# for i in range(len(xadrez)):
#     for j in range(len(xadrez)):
#         if ((i+j) % 2 == 0):
#             xadrez[i][j] = 1

# plt.imshow(xadrez, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# diagonal = gerar_matriz(8, 8)

# for i in range(len(diagonal)):
#     diagonal[i][i] = 1

# plt.imshow(diagonal, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# diagonal_contraria = gerar_matriz(8, 8)

# for i in range(len(diagonal_contraria)):
#     diagonal_contraria[i][len(diagonal_contraria) - 1 - i] = 1

# plt.imshow(diagonal_contraria, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# xis = gerar_matriz(7, 7)

# for i in range(len(xis)):
#     xis[i][i] = 1
#     xis[i][len(xis) - 1 - i] = 1
    
# plt.imshow(xis, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# triangulo = gerar_matriz(7, 7)

# for i in range(len(triangulo)):
#     for j in range(i):
#         triangulo[j][i] = 1
    
# plt.imshow(triangulo, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# trans = gerar_matriz(5, 5)

# for i in range(len(trans)):
#     for j in range(len(trans)):
#         trans[i][j] = i

# plt.imshow(trans, cmap='hot')
# plt.figure()

# for i in range(len(trans)):
#     for j in range(i):
#         aux = trans[i][j]
#         trans[i][j] = trans[j][i]
#         trans[j][i] = aux

# plt.imshow(trans, cmap='hot')
# plt.show()

'''--------------------------------------------------'''

# pesos = [1, 2, 3, 2, 1]

# notas = [[10, 7], [9, 2], [5, 9], [3, 1], [10, 0]]

# soma_pesos = 0
# for e in pesos:
#     soma_pesos += e

# medias = []
# for j in range(len(notas[0])):
#     soma = 0
#     for i in range(len(pesos)):
#         soma += pesos[i] * notas[i][j]
#     medias.append(soma / soma_pesos)

# print(medias)

'''--------------------------------------------------'''

circulo = gerar_matriz(1000, 1000)
for i in range(len(circulo)):
    for j in range(len(circulo)):
        if ((i-len(circulo)//2)**2 + (j-len(circulo)//2)**2 < (len(circulo)//2)**2):
            circulo[i][j] = i+j

plt.imshow(circulo)
plt.show()
