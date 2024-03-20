'''
11. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
  - Se a soma soma dos ângulos for diferente de 180º escrever que não é um triângulo
  - Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
  - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
  - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
'''

contador = 1
angulo1 = int(input(f'Digite a medida do {contador}º ângulo de um triângulo: '))
contador = contador + 1
angulo2 = int(input(f'Digite a medida do {contador}º ângulo de um triângulo: '))
contador = contador + 1
angulo3 = int(input(f'Digite a medida do {contador}º ângulo de um triângulo: '))
tipo = ''
if (angulo1 + angulo2 + angulo3 != 180):
  print('Não é um triângulo')
else:
  if (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
      tipo = 'Retângulo'
  elif (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
      tipo = 'Obtusângulo'
  else:
      tipo = 'Acutângulo'
  print(f'Um triângulos com essas medidas dos ângulos é um Triângulo {tipo}')
