# Peça dois números ao usuário
# Printe a divisão entre eles
# Cuide dos casos de não digitar um número e divisão por zero

while True:
  try:
    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))
    resultado1 = num1/num2
    resultado2 = num2/num1
  except ValueError:
    print('Necessário digitar um número!')
  except ZeroDivisionError:
    print('Não existe divisão por 0 (zero)!')
  except Exception as e:
    print(e)
    print(type(e))
  else:
    print(f'{num1} / {num2} = {resultado1}')
    print(f'{num2} / {num2} = {resultado2}')
    break