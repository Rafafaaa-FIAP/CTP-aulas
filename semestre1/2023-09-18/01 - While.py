# usuario = 'danilo'
# senha = '1234'
# tentativas = 1
# usuarioDigitado = input('Digite o usuário: ')
# senhaDigitado = input('Digite a senha: ')

# # while ((usuario != usuarioDigitado or senha != senhaDigitado) and tentativas < 3):
# while (not(usuario == usuarioDigitado and senha == senhaDigitado) and tentativas < 3):
#   print(f'Você tem mais {3-tentativas} tentativas')
#   usuarioDigitado = input('Diga seu usuário: ')
#   senhaDigitado = input('Digite a senha: ')
#   tentativas += 1
  
# if (usuario == usuarioDigitado and senha == senhaDigitado):
#   print('Acesso liberado')
# else:
#   print('Limite de tentativas atingido')

'''--------------------------------------------------'''

# i = 0
# soma = 0
# while (i < 10):
#   soma += float(input(f'Digite o {i+1}º número: '))
#   i += 1
# print(f'A média dos número digitados é {soma / i}')

'''--------------------------------------------------'''

# i = 0
# qtdPar = 0
# qtdImpar = 0
# while (i < 10):
#   if (int(input(f'Digite o {i+1}º número: ')) % 2 == 0):
#     qtdPar += 1
#   else:
#     qtdImpar += 1
#   i += 1
# print(f'A quantidade de números pares digitados é {qtdPar}')
# print(f'A quantidade de números ímpares digitados é {qtdImpar}')

'''--------------------------------------------------'''

num = int(input('De qual você quer saber a tabuada? '))
i = 1
while (i <= 10):
  print(f'{num} X {i} = {num*i}')
  i += 1