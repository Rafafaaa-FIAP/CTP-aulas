'''
7 - Uma matriz retangular da forma 5xN (5 linhas e N colunas) representa as notas de alunos em 5 provas. Cada linha é a nota de um aluno em uma das provas, enquanto cada coluna representa as 5 notas de um aluno somente.

              |10  3 ... 10|
              | 9  7 ...  3|
[1 2 3 4 5] * | 5  9 ...  6|
              | 2  1 ...  4|
              | 8 10 ...  9|

Cada nota deve ser ponderada pelo peso desta matéria, representada pelo vetor de pesos à esquerda. Escreva um código que realiza esta operação e retorna uma lista com a média de cada aluno.
'''

pesos = [1, 2, 3, 4, 5]

soma_pesos = 0
for e in pesos:
    soma_pesos += e

notas = [[10, 3, 10], [9, 7, 3], [5, 9, 6], [2, 1, 4], [8, 10, 9]]

medias = []
for i in range(len(notas[0])):
    soma = 0
    for j in range(len(pesos)):
        soma += notas[j][i] * pesos[j]
    medias.append(soma / soma_pesos)

print(medias)
