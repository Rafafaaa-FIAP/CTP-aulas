'''
1 - Faça uma função que printa uma matriz da maneira convencional, ou seja, uma linha abaixo da outra.
'''

def printarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

m = [[1,2,3],[4,5,6]]
printarMatriz(m)