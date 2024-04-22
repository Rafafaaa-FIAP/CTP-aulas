'''
5 - Pergunte ao usuário se ele gostaria de cadastrar um novo carro e implemente esta funcionalidade
'''

carros = {
  'nomes' : ['celta','up','kombi','uno'],
  'portas' : [4,2,6,2],
  'preço' : [1000,200,300,100],
  'ano de fabricação' : [2014,2018,1970,2005]
}

def inputWithValidation(inputText, options):
  inputText += f'\n{'\n'.join(options)}\n'
  ret = input(inputText)
  while (ret not in options):
    print('Opção inválida!')
    ret = input(inputText)
  return ret

def cadastrarCarro():
  for key in carros.keys():
    value = input(f'{key}: ')
    carros[key].append(value)
  return

resp = inputWithValidation('Deseja cadastrar um novo carro?', ['sim', 'não'])
if (resp == 'sim'):
  cadastrarCarro()
else:
  print('Obrigado por utilizar nosso sistema!')