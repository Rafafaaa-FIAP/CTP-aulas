'''
4 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da "contra-diagonal" para 1.
'''

import defs

def contraDiagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return matriz

matriz = defs.gerarMatriz(5, 5)

defs.mostrarMatriz(contraDiagonal(matriz))