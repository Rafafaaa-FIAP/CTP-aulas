# numero = input("Diga um número: ")
# while not numero.isnumeric():
#   numero = input("Diga um número: ")
# numero = int(numero)


# while True:
#   try:
#     numero = int(input("Diga um número: "))
#     print(f'Você digitou o {numero}')
#   except:
#     print('Tem que ser um número!')
#   else:
#     print('Deu tudo certo!')
#     break


# lista = [1,2,3]
# while True:
#   try:
#     negativo  = False
#     numero = int(input('Diga um número: '))
#     if (numero < 0):
#       negativo  = True
#       raise ValueError('Não pode ser negativo!')
#     print(lista[numero])
#   except ValueError:
#     if (negativo):
#       print('Não pode ser negativo!')
#       continue
#     print('Tem que ser um número!')
#   except IndexError:
#     print(f'O número deve ser entre 0 e {len(lista) - 1}')
#   except Exception as e:
#     print(e)
#   else:
#     print('Deu tudo certo!')
#     break

'''--------------------------------------------------'''

numero = {
  1: ['um', 'one', 'uno'],
  2: ['dois', 'two', 'dos'],
  3: ['três', 'three', 'tres'],
}

while True:
  try:
    num = int(input('Digite um número: '))
    lingua = int(input('Digite a língua:\n0 - Português\n1 - Inglês\n2 - Espanhol\n'))
    print(numero[num][lingua])
  except ValueError:
    print('Tem que ser um número!')
  except IndexError:
    print('Tem que ser um número!')
  else:
    break
