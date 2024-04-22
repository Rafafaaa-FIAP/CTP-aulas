'''
8 - Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes. Ex: Eu tenho aula na sala cinco zero dois -> Eu tenho aula na sala 502
'''

numeros = {
  'zero': 0,
  'um': 1,
  'dois': 2,
  'três': 3,
  'quatro': 4,
  'cinco': 5,
  'seis': 6,
  'sete': 7,
  'oito': 8,
  'nove': 9,
}

frase = 'Eu tenho aula na sala cinco zero dois'
fraseNova = ''
print(frase)
for e in frase.split(' '):
  if (e in numeros.keys()):
    fraseNova += str(numeros[e])
  else:
    fraseNova += f'{e} '
print(fraseNova)