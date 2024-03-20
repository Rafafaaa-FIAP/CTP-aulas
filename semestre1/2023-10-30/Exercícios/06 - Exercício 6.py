'''
6 - Intersecção de Listas: Escreva uma função que recebe duas listas como entrada e retorna uma nova lista contendo elementos que são comuns em ambas as listas.
'''

def intersec_listas(lista1, lista2):
    ret = []
    for v1 in lista1:
        flag = False
        for v2 in ret:
            if (v2 == v1):
                flag = True
                break
        if (not flag):
            for v2 in lista2:
                if (v2 == v1):
                    ret.append(v1)
                    break
    return ret
print(intersec_listas([0,7,5,2,1,0], [2,3,0])) # Resultado esperado: [0,2]
