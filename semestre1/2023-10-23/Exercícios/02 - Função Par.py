'''
Faça uma função que recebe uma lista e retorna a quantidade de numeros pares ali dentro
'''

def qtdPares(numeros):
    qtd = 0
    for elem in numeros:
        if (elem % 2 == 0):
            qtd += 1
    return qtd

print(qtdPares([1,2,3,4,5,6]))