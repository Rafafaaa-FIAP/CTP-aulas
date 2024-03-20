
def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

'''--------------------------------------------------'''

# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# # printa_matriz(matriz)

# # print(matriz[0][2])

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         matriz[i][j] = 1

# printa_matriz(matriz)

'''--------------------------------------------------'''

# matriz = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if (i == j):
#             matriz[i][j] = 1
#         else:
#             matriz[i][j] = 0

# printa_matriz(matriz)

'''--------------------------------------------------'''

# matriz = []

# for i in range(8):
#     linha = []
#     for j in range(8):
#         if (i % 2 == 0):
#             if (j % 2 == 0):
#                 linha.append(1)
#             else:
#                 linha.append(0)
#         else:
#             if (j % 2 == 0):
#                 linha.append(0)
#             else:
#                 linha.append(1)
#     matriz.append(linha)

# printa_matriz(matriz)


import matplotlib.pyplot as plt

matriz = []

for i in range(8):
    linha = []
    for j in range(8):
        if ((i + j) % 2 == 0):
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

printa_matriz(matriz)

plt.imshow(matriz, cmap='hot')
plt.show()

# python -m venv env
# .\env\Scripts\activate
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# python -m pip install --upgrade pip
# clicar no play
