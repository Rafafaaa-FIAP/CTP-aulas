'''
5. Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
'''

contador = 1
a = int(input(f'Digite o {contador}º valor: '))
contador = contador + 1
b = int(input(f'Digite o {contador}º valor: '))
contador = contador + 1
c = int(input(f'Digite o {contador}º valor: '))
ordem = ''
#--> Maneira feita por mim
# if (a < b and a < c):
#     if (b < c):
#         ordem = f'{a}, {b}, {c}'
#     else:
#         ordem = f'{a}, {c}, {b}'
# elif (b < c):
#     if (a < c):
#         ordem = f'{b}, {a}, {c}'
#     else:
#         ordem = f'{b}, {c}, {a}'
# else:
#     if (a < b):
#         ordem = f'{c}, {a}, {b}'
#     else:
#         ordem = f'{c}, {b}, {a}'

#--> maneira feita pelo professor
if (a > b and a > c):
  pass
elif (b > c):
  aux = a
  a = b
  b = aux
else:
  aux = a
  a = c
  c = aux
if (b > c):
  ordem = f'{c}, {b}, {a}'
else:
  ordem = f'{b}, {c}, {a}'
print(f'A ordem crescente dos valores é: {ordem}')
