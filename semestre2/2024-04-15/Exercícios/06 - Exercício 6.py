'''
6 - Pergunte ao usuário se ele gostaria de remover um carro e implemente esta funcionalidade
'''

carros = {
  'nomes' : ['celta','up','kombi','uno'],
  'portas' : [4,2,6,2],
  'preço' : [1000,200,300,100],
  'ano de fabricação' : [2014,2018,1970,2005]
}

def atualizarIndices():
    indices = {carros['nomes'][i] : i for i in range(len(carros['nomes'])) }
    return indices

dicIndices = atualizarIndices()

def inputWithValidation(inputText, options):
  inputText += f'\n{'\n'.join(options)}\n'
  ret = input(inputText)
  while (ret not in options):
    print('Opção inválida!')
    ret = input(inputText)
  return ret

def removerCarro():
  carro = inputWithValidation('Qual carro deseja remover:', carros['nomes'])
  indice_remover = dicIndices[carro]
  for key in carros.keys():
    carros[key].pop(indice_remover)
  return

print(carros)
resp = inputWithValidation('Deseja remover um carro?', ['sim', 'não'])
if (resp == 'sim'):
  removerCarro()
  dicIndices = atualizarIndices()
else:
  print('Obrigado por utilizar nosso sistema!')
print(carros)