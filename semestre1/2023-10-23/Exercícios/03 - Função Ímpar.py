'''
Faça uma função que recebe uma lista e retorna a quantidade de numeros ímpares ali dentro
'''

def qtdImpares(numeros):
    qtd = 0
    for elem in numeros:
        if (elem % 2 != 0):
            qtd += 1
    return qtd

print(qtdImpares([1,2,3,4,5,6]))