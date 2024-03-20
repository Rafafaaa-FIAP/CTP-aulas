'''
1. Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.
'''

contador = 1
value1 = int(input(f'Digite o {contador}º valor: '))
contador = contador + 1
value2 = int(input(f'Digite o {contador}º valor: '))
maior = 0
if (value1 > value2):
    maior = value1
else:
    maior = value2
print(f'O maior valor é: {maior}')
