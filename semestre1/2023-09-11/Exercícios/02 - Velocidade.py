velocidade = float(input('Digite a velocidade: '))
if (velocidade < 0):
  print('Velocidade inválida')
elif (velocidade <= 80):
  print('Velocidade permitida')
else:
  if (velocidade <= 100):
    multa = (velocidade - 80) * 5
  elif (velocidade <= 120):
    multa = ((velocidade - 100) * 10) + 100
  else:
    multa = ((velocidade - 120) * 20) + 300
  print (f'O valor da multa é de R${multa}')