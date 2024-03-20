'''
8 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

qtd = int(input('Digite a quantidade de termos da série de Fibonacci deseja ver: '))

i = 0
numAnt = 0
numAtual = 1
print(numAtual)
while (i < qtd):
  aux = numAtual
  numAtual = numAtual + numAnt
  numAnt = aux
  print(numAtual)
  i += 1

# Método do professor
# i = 0
# a = 0
# b = 1
# c = 0
# while (i < qtd):
#   c = a + b
#   a = b
#   b = c
#   print(c)
#   i += 1