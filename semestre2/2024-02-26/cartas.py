
import matplotlib.pyplot as plt

def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def cria_linha(indice, qtd):
    lista = []
    for i in range(qtd):
        lista.append(0)
    lista[indice] = 1
    return lista

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
v = [11,9,12,1,13,3,5,2,6,4,7,10,8]
embaralhar = []

for k in range(len(a)):
    elem = a[k]
    for i in range(len(v)):
        if (v[i] == elem):
            indice = i
            lista = cria_linha(indice, len(v))
            break
    embaralhar.append(lista)
printa_matriz(embaralhar)

plt.imshow(embaralhar, cmap='hot')
plt.show()