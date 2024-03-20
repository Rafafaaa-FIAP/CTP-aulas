# senha = input('Diga sua senha: ')
# senha_correta = '1234'
# limite = 5
# tentativas = 1
# while (senha != senha_correta and tentativas < limite):
#   print(f'Errou! Mais {limite-tentativas} tentativas')
#   senha = input('Diga sua senha: ')
#   tentativas += 1
  
# if (senha == senha_correta):
#   print('Acesso liberado')
# else:
#   print('Sai hacker')

'''--------------------------------------------------'''

# pergunta = 'Digite s ou n: '
# opcao = input(pergunta)
# while (opcao != 's' and opcao != 'n'):
#   print('Opção inválida')
#   opcao = input(pergunta)
# print(opcao)

# pergunta = 'Digite s ou n: '
# opcao = input(pergunta)
# while (not(opcao == 's' or opcao == 'n')):
#   print('Opção inválida')
#   opcao = input(pergunta)
# print(opcao)

'''--------------------------------------------------'''

# pergunta = 'Deseja conhecer minha calculadora? (s/n): '
# opcao = input(pergunta)
# while (opcao != 's' and opcao != 'n'):
#   print('Opção inválida!')
#   opcao = input(pergunta)
# if (opcao == 'n'):
#   print('Tudo bem ;-;')
# else:
#   num1 = float(input('Digite o 1º número: '))
#   num2 = float(input('Digite o 2º número: '))
#   pergunta = 'Qual operação deseja fazer? (+, -, *, /): '
#   opcao = input(pergunta)
#   while (opcao != '+' and opcao != '-' and opcao != '*' and opcao != '/'):
#     print('Opção inválida!')
#     opcao = input(pergunta)
#   if (opcao == '+'):
#     resultado = num1 + num2
#   elif (opcao == '-'):
#     resultado = num1 - num2
#   elif (opcao == '*'):
#     resultado = num1 * num2
#   else:
#     resultado = num1 / num2
#   print(f'O resulta de {num1} {opcao} {num2} é igual a {resultado}')
