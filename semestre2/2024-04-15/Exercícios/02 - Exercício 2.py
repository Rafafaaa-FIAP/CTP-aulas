'''
2 - Traga ao usuário todas as informações sobre um carro de sua escolha:

carros = {
  'nomes' : ['celta','up','kombi','uno'],
  'portas' : [4,2,6,2],
  'preço' : [1000,200,300,100],
  'ano de fabricação' : [2014,2018,1970,2005]
}
'''

carros = {
  'nomes' : ['celta','up','kombi','uno'],
  'portas' : [4,2,6,2],
  'preço' : [1000,200,300,100],
  'ano de fabricação' : [2014,2018,1970,2005]
}

indices = {carros['nomes'][i] : i for i in range(len(carros['nomes']))}

def inputWithValidation(inputText, options):
  inputText += f'\n{'\n'.join(options)}\n'
  ret = input(inputText)
  while (ret not in options):
    print('Opção inválida!')
    ret = input(inputText)
  return ret

carro = inputWithValidation(f'Digite o carro que deseja ver:', carros['nomes'])
print('\nInformações:\n')
for key in carros.keys():
  print(f'{key}: {carros[key][indices[carro]]}')
