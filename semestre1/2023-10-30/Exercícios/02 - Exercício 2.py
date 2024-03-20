'''
2 - Números Pares: Escreva uma função que recebe uma lista de números como entrada e retorna uma nova lista contendo apenas os números pares da lista original.
'''

def pares_lista(lista):
    ret = []
    for value in lista:
        if (value % 2 == 0):
            ret.append(value)
    return ret
print(pares_lista([1,2,3,4,5]))
