'''
10 - Devido a covid as cadeiras de cinema tem que ser utilizadas com um espaçamento de uma cadeira desocupada tanto na frente quanto atrás e dos lados. Represente esta situação com uma matriz 50x50 em que cada local (i,i) tem nele a palavra "vaga" ou ocupada.
'''

import defs

matriz = defs.gerarMatriz(50, 50)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = 'vaga'

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if ((i+j) % 2 == 0):
            matriz[i][j] = 'ocupada'

defs.mostrarMatriz(matriz)