'''
6. Tendo como entrada a altura e sexo (codificando da seguinte forma: 1:feminino   2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
  - para homens: (72.7 * Altura) – 58
  - para mulheres: (62.1 * Altura) – 44.7
'''

altura = float(input('Digite sua altura: '))
sexo = int(input('Digite seu sexo (1-Masculino | 2-Feminino): '))
peso = 'Seu peso ideial é: '
if (sexo == 1):
    peso = peso + str(round((72.2 * altura) - 58, 2))
elif (sexo == 2):
    peso = peso + str(round((62.1 * altura) - 44.7, 2))
print(peso)
