qtd = int(input('Digite a quantidade de termos da série de Fibonacci deseja ver: '))

i = 0
a = 1
b = 1
c = 0
qtdPrimo = 0
while (i < qtd):
  c = a + b
  a = b
  b = c
  print(c)
  i += 1
  
  j = 1
  isPrimo = True
  while (True):
    #print(f'{c} % {j} = {c % j}')
    if (j > c ** 0.5):
      break
    elif (c % j == 0 and j != 1 and j != c):
      isPrimo = False
      break
    j += 1
  if (isPrimo):
    qtdPrimo += 1
    
print(f'A quantidade de números primos dos primeiros {qtd} números da série de Fibonacci é {qtdPrimo}')
  
