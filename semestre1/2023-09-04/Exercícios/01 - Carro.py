'''
Pegue de input a velicidade de um carro
  - Se ele estiver acima de 80 e abaixo de 100, cobre 5 reais de multa para cada km/h acima de 80km/h
  - Se ele estiver entre 100 e 120, cobre 10 reais de multa para cada km/h a mais
  - Se ele estiver acima de 120, cobre 20 reais de multa para cada km/h a mais
'''

velocidade = float(input('Digite a velocidade de um carro: '))

if (velocidade < 0):
  print('Velocidade inválida')
elif (velocidade <= 80):
  print('Velocidade permitida')
else:
  if (velocidade <= 100):
    multa = (velocidade - 80) * 5
  elif (velocidade <= 120):
    multa = ((velocidade - 100) * 10) + (100)
  else:
    multa = ((velocidade - 120) * 20) + (100) + (200)
  print(f'O valor da multa é de R$ {multa}')