resposta = input('Você trabalha? (s/n) ')
if (resposta == 's'):
  salario = float(input('Diga seu salário: '))
  if (salario <= 2112):
    aliquota = 0
  elif (salario <= 2826.65):
    aliquota = 7.5
  elif (salario <= 3751.05):
    aliquota = 15
  elif (salario <= 4664.68):
    aliquota = 22.5
  else:
    aliquota = 27.5
  aliquota = aliquota / 100
  desconto = salario * aliquota
  restante = salario - desconto
  print(f'Você receberá R${restante}')
else:
  print('Seu herdeiro')