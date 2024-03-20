'''
9. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.
'''

contador = 1
value1 = int(input(f'Digite o {contador}º valor: '))
contador = contador + 1
value2 = int(input(f'Digite o {contador}º valor: '))
contador = contador + 1
value3 = int(input(f'Digite o {contador}º valor: '))
maior = 0
if (value1 > value2 and value1 > value3):
    maior = value1
elif (value2 > value3):
    maior = value2
else:
    maior = value3
print(f'O maior valor é: {maior}')
