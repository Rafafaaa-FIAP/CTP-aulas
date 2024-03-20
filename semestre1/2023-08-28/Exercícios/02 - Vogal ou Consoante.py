'''
Faça um programa para ler uma letra e escrever se é uma vogal ou consoante.
'''

letra = input('Digite uma letra: ')
tipo = ''
if (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or
    letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    tipo = 'vogal'
else:
    tipo = 'consoante'
print(f'A letra digitada é uma {tipo}.')
