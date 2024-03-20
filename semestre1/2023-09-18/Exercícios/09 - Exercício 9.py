'''
9 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
'''

i = 0
qtdPar = 0
qtdImpar = 0
while (i < 10):
  if (int(input(f'Digite o {i+1}º número: ')) % 2 == 0):
    qtdPar += 1
  else:
    qtdImpar += 1
  i += 1
print(f'A quantidade de números pares digitados é {qtdPar}')
print(f'A quantidade de números ímpares digitados é {qtdImpar}')