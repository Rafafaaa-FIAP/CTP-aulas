'''
4 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma = 0
i = 0
while (i < 5):
  soma += float(input(f'Digite o {i+1}º número: '))
  i += 1
print(f'A soma dos número digitados é {soma}')
print(f'A média dos número digitados é {soma/i}')