'''
7- Escreva um código capaz de contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:

O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.
'''

frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.'

frase = frase.lower()
for char in ',.':
    frase = frase.replace(char,'')
frase_lista = frase.split(' ')

inputText = 'Digite uma palavra: '
palavra = input(inputText)
while (palavra == ''):
  palavra = input(inputText)

count = 0
for p in frase_lista:
  if (p == palavra):
    count += 1

if (count == 0):
  print(f'A palavra {palavra} não aparece nenhuma vez!')
else:
  print(f'A palavra {palavra} aparece {count} vez(es)!')
