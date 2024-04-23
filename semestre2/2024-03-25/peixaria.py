
# 1 - Cadastrar novo produto
# 2 - Remover um produto
# 3 - Atualizar infos de um produto
# 4 - Trazer todos as infos sobre um produto

peixes = {
  'Espécie': ['Tilápia', 'Baiacu', 'Tucunaré', 'Lambaqui' , 'Salmão', 'Bacalhau', 'Truta'],
  'Valor': [25, 30, 20, 101, 45, 60, 15],
  'Região': ['Piracicaba', 'Oceania', 'Amazonas', 'Águas Raras', 'Noruega', 'Portugal', 'Zona Leste'],
  'Estoque': [10, 23, 3, 31, 42, 12, 21],
  'Validade': [9, 2, 10, 11, 7, 6, 3]
}

menu = ['Cadastrar', 'Remover', 'Atualizar', 'Ver Informações', 'Sair']

indices = []

def main():
  global indices
  indices = atualizarIndices()
  print('Bem-vindo a peixaria!')

  menu_selecionado = selecionarMenu()
  while (menu_selecionado != 'Sair'):
    print(f'|----- {menu_selecionado} -----|')
    if (menu_selecionado == 'Cadastrar'):
      cadastrar()
      indices = atualizarIndices()
    elif (menu_selecionado == 'Remover'):
      remover()
      indices = atualizarIndices()
    elif (menu_selecionado == 'Atualizar'):
      atualizar()
    elif (menu_selecionado == 'Ver Informações'):
      verInformacoes()
    menu_selecionado = selecionarMenu()

  print('Obrigado por utilizar nosso sistema!')

  return

def inputWithValidation(inputText, options, showOptions = False):
  if (showOptions):
    inputText += f'\n{'\n'.join(options)}\n'
  ret = input(inputText)
  while (ret not in options):
    print('Opção inválida!')
    ret = input(inputText)
  return ret

def atualizarIndices():
  return {peixes['Espécie'][i] : i for i in range(len(peixes['Espécie']))}

def selecionarMenu():
  print('|----- MENU -----|')
  for m in menu:
    print(m)

  return inputWithValidation('', menu)

def cadastrar():
  for key in peixes.keys():
    info = input(f'Informe a/o {key}: ')
    peixes[key].append(info)
  
  print('Peixe cadastrado!')

  return

def remover():
  peixe_remover = inputWithValidation('Qual peixe deseja remover?', peixes['Espécie'], True)
  indice = indices[peixe_remover]
  for key in peixes.keys():
    peixes[key].pop(indice)
  
  print('Peixe removido!')

  return

def atualizar():
  peixe_atualizar = inputWithValidation('Qual peixe deseja atualizar?', peixes['Espécie'], True)
  indice = indices[peixe_atualizar]
  for key in peixes.keys():
    if (key != 'Espécie'):
      info = input(f'Informe a/o novo/a {key}: ')
      peixes[key][indice] = info
  
  print('Peixe removido!')

  return

def verInformacoes():
  peixe_ver = inputWithValidation('Deseja ver as informações de qual peixe?', peixes['Espécie'], True)
  indice = indices[peixe_ver]
  for key in peixes.keys():
    print(f'{key}: {peixes[key][indice]}')

  return



main()
