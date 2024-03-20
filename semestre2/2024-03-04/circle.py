
import matplotlib.pyplot as plt

# python -m venv env
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# .\env\Scripts\activate
# python -m pip install --upgrade pip
# clicar no play

def geraMatriz(linhas, colunas):
    matriz =[]

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    print()
    return matriz

def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

matriz = geraMatriz(5, 5)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if (((i+j) % 2 == 0 and i % 2 == 0) or ((i+j) % 2 != 0 and j % 2 == 0)):
            matriz[i][j] = 1

plt.imshow(matriz, cmap='hot')
plt.show()


