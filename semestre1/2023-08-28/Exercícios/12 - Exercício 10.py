'''
10. Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
  - Triângulo Equilátero: possui os 3 lados iguais.
  - Triângulo Isóscele: possui 2 lados iguais.
  - Triângulo Escaleno: possui 3 lados diferentes.
'''

contador = 1
medida1 = int(input(f'Digite a medida do {contador}º lado de um triângulo: '))
contador = contador + 1
medida2 = int(input(f'Digite a medida do {contador}º lado de um triângulo: '))
contador = contador + 1
medida3 = int(input(f'Digite a medida do {contador}º lado de um triângulo: '))
tipo = ''
if (medida1 == medida2 and medida1 == medida3):
    tipo = 'Equilátero'
elif (medida1 == medida2 or medida1 == medida3 or medida2 == medida3):
    tipo = 'Isóseles'
else:
    tipo = 'Escaleno'
print(f'Um triângulos com essas medidas dos lados é um Triângulo {tipo}')
