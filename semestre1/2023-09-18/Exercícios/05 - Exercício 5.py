'''
5 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''

num1 = input('Digite o 1º número: ')
while (not num1.isnumeric()):
  print('Deve ser um número inteiro!')
  num1 = input('Digite o 1º número: ')
num1 = int(num1)

num2 = input('Digite o 2º número: ')
while (not num2.isnumeric()):
  print('Deve ser um número inteiro!')
  num2 = input('Digite o 2º número: ')
num2 = int(num2)

if (num1 < num2):
  numAtual = num1
  numFinal = num2
else:
  numAtual = num2
  numFinal = num1

numAtual += 1
while (numAtual < numFinal):
  print(numAtual)
  numAtual += 1

# Método do professor
# while (num1 < num2):
#   print(num1)
#   num1 += 1

# while (num2 < num1):
#   print(num2)
#   num2 += 1