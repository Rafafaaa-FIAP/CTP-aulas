'''
6 - Faça uma função que recebe uma matriz quadrada e retorna sua transposta.
'''

import defs

def transposta(trans):
    for i in range(len(trans)):
        for j in range(i):
            aux = trans[i][j]
            trans[i][j] = trans[j][i]
            trans[j][i] = aux
    return trans

matriz = defs.gerarMatriz(5, 5)

num = 1
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = num
        num += 1

defs.printarMatriz(matriz)
print('')
defs.printarMatriz(transposta(matriz))