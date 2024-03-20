'''
7. Escreva um programa para ler o número de lados de um polígono regular e imprimir o seguinte:
  - Se o número de lados for igual a 3 escrever TRIÂNGULO
  - Se o número de lados for igual a 4 escrever QUADRADO
  - Se o número de lados for igual a 5 escrever PENTÁGONO.
'''

qtd = int(input('Digite a quantidade de lados de um polígono regular: '))
tipo = ''
if (qtd == 3):
    tipo = 'TRIÂNGULO'
elif (qtd == 4):
    tipo = 'QUADRADO'
elif (qtd == 5):
    tipo = 'PENTÁGONO'
print(tipo)
