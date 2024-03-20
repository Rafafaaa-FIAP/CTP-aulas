'''
8 - Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez.
'''

import defs

matriz = defs.gerarMatriz(8, 8)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if ((i+j) % 2 == 0):
            matriz[i][j] = 1

defs.mostrarMatriz(matriz)