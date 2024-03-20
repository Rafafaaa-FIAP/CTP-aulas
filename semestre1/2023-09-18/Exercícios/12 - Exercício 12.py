'''
12 - Faça um programa que calcule o mostre a média aritmética de N notas.
'''

qtdNota = int(input('Digite a quantidade de notas: '))
i = 0
soma = 0
while (i < qtdNota):
  soma += float(input(f'Digite a {i+1}ª nota: '))
  i += 1
print(f'A média é {soma/qtdNota}')