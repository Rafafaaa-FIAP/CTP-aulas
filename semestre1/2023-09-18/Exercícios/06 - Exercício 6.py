'''
6 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

showError = False
usuario = ''
senha = ''
while (usuario == senha):
  if (showError):
    print('Usuário e senha não podem ser iguais!')
  usuario = input('Digite o usuário: ')
  senha = input('Digite a senha: ')
  showError = True
print(f'Usuário: {usuario}')
print(f'Senha: {senha}')