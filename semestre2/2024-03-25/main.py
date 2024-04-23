#1 - Cria um dicionário vazio
#2 - Crie uma chave par e associe a uma lista vazia
#3 - Crie uma chave ímpar e associe a uma lista vazia
#4 - Preencha cada chave com os números pares/ímpares de 0 a 10

# dic = {}
# dic['pares'] = []
# dic['impares'] = []

# for i in range(10):
#   if (i % 2 == 0):
#     dic['pares'].append(i)
#   else:
#     dic['impares'].append(i)

# print(dic)

'''--------------------------------------------------'''

#1 - Crie uma dicionário com 4 chaves, nome de carros e seus preços
#2 - Printe as chaves e seu conteúdo usando um for

# carros = {
#   'celta': 1000,
#   'gol': 100,
#   'ka': 50,
#   'uno': 999
# }

# for key in carros.keys():
#   print(f'O {key} custa R$ {carros[key]}')

'''--------------------------------------------------'''

# dic1 = {
#   'paises': ['Brasil', 'Colombia', 'Inglaterra', 'Uruguai', 'Argentina'],
#   'populacao': [10000, 200, 30000, 2000, 40000],
#   'pib': [4, 2, 1,6, 7]
# }

# dic2 = {
#   'idh': [3, 7, 1, 2, 5],
#   'populacao': [10000, 200, 30000, 2000, 40000],
#   'pib': [4, 2, 1,6, 7],
#   'copas do mundo': [5, 0, 1, 1, 3]
# }

# igual = {}
# diferente = {}

# for key in dic1.keys():
#   if (key in dic2.keys()):
#     igual[key] = dic1[key]
#   else:
#     diferente[key] = dic1[key]

# for key in dic2.keys():
#   if (key not in dic1.keys()):
#     diferente[key] = dic2[key]

# print(igual)
# print(diferente)

'''--------------------------------------------------'''

# vogais = {
#   'àáãâ': 'a',
#   'éê': 'e'
# }

frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
# for key in vogais.keys():
#   for char in key:
#     frase = frase.replace(char, vogais[key])
# print(frase)
frase = frase.replace('.', '')
print(frase)
frase = frase.lower()
print(frase)
frase = frase.split(' ')
print(frase)

dic = {}
for e in frase:
  if (e not in dic.keys()):
    dic[e] = 1
  else:
    dic[e] += 1
print(dic)




# indices = {peixes["Espécies"][i] : i for i in range(len(peixes["Espécies"]))}
# def obriga_opcao(lista,msg, msg_erro = None):
#     resp = input(msg)
#     while resp not in lista:
#         print("Diga uma opção cadastrada!")
#         if msg_erro:
#             print(msg_erro)
#         resp = input(msg)
#     return resp

# def atualizar():
#     qual = obriga_opcao(indices.keys(),"Qual peixe vc quer atualizar?",'\n'.join(peixes['Espécies']))
#     indice = indices[qual]
#     for key in peixes.keys():
#         peixes[key][indice] = input(f"Diga o novo {key}")
#     return

# def cadastrar():
#     for key in peixes.keys():
#         info = input(f'Diga o/a novo/a {key}: ')
#         peixes[key].append(info)
#     return

# def infos():
#     qual = obriga_opcao(indices.keys(),"Qual peixe vc quer ver?",'\n'.join(peixes['Espécies']))
#     indice = indices[qual]
#     for key in peixes.keys():
#         print(f"{key} : {peixes[key][indice]}")
#     return

# def remover():
#     qual = obriga_opcao(indices.keys(),"Qual peixe vc quer remover?",'\n'.join(peixes['Espécies']))
#     indice = indices[qual]
#     for key in peixes.keys():
#         peixes[key].pop(indice)
#     return

# infos()