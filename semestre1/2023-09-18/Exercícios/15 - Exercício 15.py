'''
15 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
  1, 2, 3, 4 - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
  5 - Voto Nulo
	6 - Voto em Branco
  
  Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
  	O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

print('1-José')
print('2-João')
print('3-Roberta')
print('4-Maria')
print('5-Nulo')
print('6-Branco')
voto = 1
qtdVoto1 = 0
qtdVoto2 = 0
qtdVoto3 = 0
qtdVoto4 = 0
qtdVoto5 = 0
qtdVoto6 = 0
qtdTotal = 0
while True:
  voto = int(input('Digite seu voto: '))
  if (voto == 0):
    break
  elif (voto < 0 or voto > 6):
    print('Voto inválido!')
  else:
    qtdTotal += 1
    if (voto == 1):
      qtdVoto1 += 1
    elif (voto == 2):
      qtdVoto2 += 1
    elif (voto == 3):
      qtdVoto3 += 1
    elif (voto == 4):
      qtdVoto4 += 1
    elif (voto == 5):
      qtdVoto5 += 1
    elif (voto == 6):
      qtdVoto6 += 1
if (qtdTotal > 0):
  print('Resultados:')
  print(f'{qtdVoto1} votos para José')
  print(f'{qtdVoto2} votos para João')
  print(f'{qtdVoto3} votos para Roberta')
  print(f'{qtdVoto4} votos para Maria')
  print(f'{qtdVoto5} votos Nulo')
  print(f'{qtdVoto6} votos em Branco')
  print(f'{(qtdVoto5 * 100) / qtdTotal}% de votos Nulo')
  print(f'{(qtdVoto6 * 100) / qtdTotal}% de votos em Branco')
else:
  print('Nenhum voto válido!')