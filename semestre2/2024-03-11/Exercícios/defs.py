import matplotlib.pyplot as plt

def gerarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def printarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def mostrarMatriz(matriz):
    plt.imshow(matriz, cmap="hot")
    plt.show()
    return
