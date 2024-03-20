'''
1 - Soma de uma Lista: Escreva uma função que recebe uma lista de números como entrada e retorna a soma de todos os números na lista
'''

def soma_lista(lista):
    qtd = 0
    for value in lista:
        qtd += value
    return qtd

print(soma_lista([1,2,3]))
