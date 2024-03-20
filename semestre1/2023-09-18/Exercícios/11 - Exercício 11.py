'''
11 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

# Sem break
num = int(input('Digite um número: '))
i = 1
breakWhile = False
isPrimo = True
while (i <= num and not(breakWhile)):
  print(f'{num} % {i} = {num % i}')
  if (i > num / 2):
    breakWhile = True
  elif (num % i == 0 and i != 1 and i != num ):
    isPrimo = False
    breakWhile = True
  i += 1
if (isPrimo):
  print(f'O número {num} é primo')
else:
  print(f'O número {num} não é primo')

# Com break
i = 1
isPrimo = True
while (i <= num):
  print(f'{num} % {i} = {num % i}')
  if (i > num / 2):
    break
  elif (num % i == 0 and i != 1 and i != num):
    isPrimo = False
    break
  i += 1
if (isPrimo):
  print(f'O número {num} é primo')
else:
  print(f'O número {num} não é primo')

# Com break e raíz quadrada
i = 1
isPrimo = True
while (True):
  print(f'{num} % {i} = {num % i}')
  if (i > num ** 0.5):
    break
  elif (num % i == 0 and i != 1 and i != num):
    isPrimo = False
    break
  i += 1
if (isPrimo):
  print(f'O número {num} é primo')
else:
  print(f'O número {num} não é primo')