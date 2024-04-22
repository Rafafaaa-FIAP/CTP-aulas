
# 1 - Cadastrar novo produto
# 2 - Remover um produto
# 3 - Atualizar infos de um produto
# 4 - Trazer todos as infos sobre um produto

peixes = {
  'Espécies': ['Tilápia', 'Baiacu', 'Tucunaré', 'Lambaqui' , 'Salmão', 'Bacalhau', 'Truta'],
  'Valor': [25, 30, 20, 101, 45, 60, 15],
  'Região': ['Piracicaba', 'Oceania', 'Amazonas', 'Águas Raras', 'Noruega', 'Portugal', 'Zona Leste'],
  'Estoque': [10, 23, 3, 31, 42, 12, 21],
  'Validade': [9, 2, 10, 11, 7, 6, 3]
}

menu = {
  'Códigos': ['1', '2', '3', '4', '0'],
  'Nomes': ['Cadastrar', 'Remover', 'Atualizar', 'Ver Informações', 'Sair']
}

# def main():
#   print('Bem-vindo a peixaria!')

#   menu_id = selecionarMenu()
#   while (int(menu_id) != 0):
#     menu_id = selecionarMenu()

#   print('Obrigado por utilizar nosso sistema!')

#   return

# def selecionarMenu():
#   print('|----- MENU -----|')
#   for i in range(len(menu['Códigos'])):
#     print(f'{menu['Códigos'][i]} - {menu['Nomes'][i]}')

#   return inputComValidacao('', menu['Códigos'])

# def inputComValidacao(optionText, possibleOptions):
#   option = input(optionText)
#   while option not in possibleOptions:
#     print('Opção inválida!')
#     option = input(optionText)
    
#   return option

# main()

indices = {peixes["Espécies"][i] : i for i in range(len(peixes["Espécies"]))}
def obriga_opcao(lista,msg, msg_erro = None):
    resp = input(msg)
    while resp not in lista:
        print("Diga uma opção cadastrada!")
        if msg_erro:
            print(msg_erro)
        resp = input(msg)
    return resp

def atualizar():
    qual = obriga_opcao(indices.keys(),"Qual peixe vc quer atualizar?",'\n'.join(peixes['Espécies']))
    indice = indices[qual]
    for key in peixes.keys():
        peixes[key][indice] = input(f"Diga o novo {key}")
    return

def cadastrar():
    for key in peixes.keys():
        info = input(f'Diga o/a novo/a {key}: ')
        peixes[key].append(info)
    return

def infos():
    qual = obriga_opcao(indices.keys(),"Qual peixe vc quer ver?",'\n'.join(peixes['Espécies']))
    indice = indices[qual]
    for key in peixes.keys():
        print(f"{key} : {peixes[key][indice]}")
    return

def remover():
    qual = obriga_opcao(indices.keys(),"Qual peixe vc quer remover?",'\n'.join(peixes['Espécies']))
    indice = indices[qual]
    for key in peixes.keys():
        peixes[key].pop(indice)
    return

infos()