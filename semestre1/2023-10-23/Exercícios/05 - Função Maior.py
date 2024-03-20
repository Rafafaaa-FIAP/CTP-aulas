'''
Faça uma função que retorne o maior valor de uma lista
'''

def maiorNumero(lista):
    maior = lista[0]
    for elem in lista:
        if (elem > maior):
            maior = elem
    return maior

print(maiorNumero([1,5,2,4,8,5]))
