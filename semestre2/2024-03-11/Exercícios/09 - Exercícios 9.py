'''
9 - Faça um código que recebe uma matriz quadrada e retorna uma imagem com padrão de círculo.
'''

import defs

matriz = defs.gerarMatriz(1000, 1000)

metade = len(matriz)//2

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        criterio = ((i - metade) ** 2) + ((j - metade) ** 2)
        if (criterio <= (metade ** 2)):
            matriz[i][j] = i*j

defs.mostrarMatriz(matriz)
