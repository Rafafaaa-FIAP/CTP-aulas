'''
5 - Faça uma função que recebe uma matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1.
'''

import defs

def abaixoDiagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return matriz

def acimaDiagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[j][i] = 1
    return matriz
    
matriz = defs.gerarMatriz(5, 5)
defs.mostrarMatriz(abaixoDiagonal(matriz))

matriz = defs.gerarMatriz(5, 5)
defs.mostrarMatriz(acimaDiagonal(matriz))