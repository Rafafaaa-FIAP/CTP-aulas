import requests

cep = input('Digite um CEP: ')

endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

print()

for key in endereco.keys():
  print(f'{key}: {endereco[key]}')