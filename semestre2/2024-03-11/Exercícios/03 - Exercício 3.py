'''
3 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal para 1.
'''

import defs

def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return matriz

matriz = defs.gerarMatriz(5,5)

defs.mostrarMatriz(diagonal(matriz))
