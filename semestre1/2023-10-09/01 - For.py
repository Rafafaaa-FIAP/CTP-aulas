
# for i in range(10):
#   print(i)

# for char in "danilo":
#   print(char)

'''--------------------------------------------------'''

#--> Com While
# usuario = 'teste'
# senha = '1234'
# usuario_teste = input('Digite seu usuario:')
# senha_teste = input('Digite sua senha:')
# tentativas = 1

# while (usuario != usuario_teste or senha != senha_teste) and tentativas < 3:
#   print(f"Restam {3 - tentativas} tentativas")
#   usuario_teste = input('Digite seu usuario:')
#   senha_teste = input('Digite sua senha:')
#   tentativas += 1

#--> Com For
# usuario = 'teste'
# senha = '1234'
# tentativas = 3

# for i in range(tentativas):
#   usuario_teste = input('Digite seu usuario:')
#   senha_teste = input('Digite sua senha:')
#   if (usuario == usuario_teste and senha == senha_teste):
#     break
#   print(f"Restam {tentativas - (i + 1)} tentativas")

'''--------------------------------------------------'''

# for i in [1,2,3,'teste']:
#   print(i)

# for i in range(0,10,2):
#   print(i)

for i in range(10,0,-2):
  print(i)
