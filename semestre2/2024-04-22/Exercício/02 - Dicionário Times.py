times = {
  'Palmeiras': 'Maior de Todos',
  'São Paulo': 'Trika',
  'Santos': 'Terceira Idade',
  'Corinthians': 'Ladrão'
}

while True:
  try:
    resposta = input('Diga seu time: ')
    print(f'Você é {times[resposta]}')
  except KeyError:
    frase = '\n'.join(times.keys())
    print(f'{resposta} não está dentre as opções:\n{frase}')
  except Exception as e:
    print(e)
    print(type(e))
  else:
    break