'''
7 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

num = 0
while (not(num >= 1 and num <= 10)):
  num = int(input('Digite um número entre 1 e 10 para ver a tabuada: '))

print(f'A tabuada do {num} é: ')
i = 1
while (i <= 10):
  print(f'{num} X {i} = {num*i}')
  i += 1

# Tabuada de todo os números
# num = 1
# while (num <= 10):
#   print(f'A tabuada do {num} é: ')
#   i = 1
#   while (i <= 10):
#     print(f'{num} X {i} = {num*i}')
#     i += 1
#   num += 1