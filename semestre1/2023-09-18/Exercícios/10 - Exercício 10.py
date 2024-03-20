'''
10 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

num = int(input('Digite um número para ver o fatorial dele: '))
fatorial = 1
i = 0
while (i < num):
  fatorial *= num - i
  i += 1  
print(f'O fatorial do número digitado é {fatorial}')