'''
2 - Faça uma função que recebe de parâmentros as dimensões (linhas e colunas) e retorna uma matriz preenchida de zeros com essas dimensões.
'''

import defs

def gerarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

defs.printarMatriz(gerarMatriz(2, 3))
