'''
14 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

num = 0
qtdIntervalo1 = 0
qtdIntervalo2 = 0
qtdIntervalo3 = 0
qtdIntervalo4 = 0
while (num >= 0):
  num = int(input('Digite um número (digite um número negativo para finalizar): '))
  if (num >= 0):
    if (num < 25):
      qtdIntervalo1 += 1
    elif (num < 50):
      qtdIntervalo2 += 1
    elif (num < 75):
      qtdIntervalo3 += 1
    elif (num < 100):
      qtdIntervalo4 += 1
print(f'A quantidade de número do intervalo [0-25] é {qtdIntervalo1}')
print(f'A quantidade de número do intervalo [26-50] é {qtdIntervalo2}')
print(f'A quantidade de número do intervalo [51-75] é {qtdIntervalo3}')
print(f'A quantidade de número do intervalo [76-100] é {qtdIntervalo4}')