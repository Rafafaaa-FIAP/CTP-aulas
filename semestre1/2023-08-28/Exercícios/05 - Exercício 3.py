'''
3. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: 
  ACESO PERMITIDO caso a senha seja válida.
  ACESSO NEGADO caso a senha seja inválida.
'''

senha = int(input('Digite a senha: '))
if (senha == 1234):
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')
