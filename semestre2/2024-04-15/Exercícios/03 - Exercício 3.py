'''
3 - Use o dicionário do item anterior para trazer todas as informações sobre o carro mais caro
'''

carros = {
  'nomes' : ['celta','up','kombi','uno'],
  'portas' : [4,2,6,2],
  'preço' : [1000,200,300,100],
  'ano de fabricação' : [2014,2018,1970,2005]
}

indiceMaisCaro = 0
for i in range(len(carros['preço'])):
  if (carros['preço'][i] > carros['preço'][indiceMaisCaro]):
    indiceMaisCaro = i

print('\nInformações do carro mais caro:\n')
for key in carros.keys():
  print(f'{key}: {carros[key][indiceMaisCaro]}')