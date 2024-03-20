'''
2 - Faça um programa que leia e valide as seguintes informações:
  a. Nome: maior que 3 caracteres;
  b. Idade: entre 0 e 150;
  c. Salário: maior que zero;
  d. Sexo: 'f' ou 'm';
  e. Estado Civil: 's', 'c', 'v', 'd';
'''

inputText = 'Digite seu nome: '
nome = input(inputText)
while (len(nome) <= 3):
  print('Digite um nome maior que 3 caracteres!')
  nome = input(inputText)

inputText = 'Digite sua idade: '
idade = int(input(inputText))
while (idade < 0 or idade > 150):
  print('Digite uma idade entre 0 e 150!')
  idade = int(input(inputText))

inputText = 'Digite seu salário: '
salario = float(input(inputText))
while (salario <= 0):
  print('Digite um salário maior que 0!')
  salario = float(input('Digite seu salário: '))

inputText = 'Digite seu sexo: '
sexo = input(inputText)
while (sexo != 'f' and sexo != 'm'):
  print('Digite f-feminino ou m-masculino!')
  sexo = input(inputText)

inputText = 'Digite seu estado civil: '
estadoCivil = input(inputText)
while (estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd'):
  print('Digite s-solteiro(a), c-casado(a), v-viúvo(a) ou d-divorciado(a)!')
  estadoCivil = input('Digite seu estado civil: ')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estadoCivil}')