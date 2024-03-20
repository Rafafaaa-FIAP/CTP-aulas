
import pandas as pd

# dicionario = {
#     'Professor': 'Danilo',
#     'Idade': 27,
#     'Carro': 'Celtinha',
#     'Disciplina': 'Python',
#     'Curso': 'Engenharia de Software'
# }

# print(dicionario)
# print(dicionario['Professor'])

# dicionario['Turma'] = '1ESPR'

# print(dicionario)
# print(dicionario['Turma'])

# for e in dicionario.keys():
#     print(dicionario[e])

'''--------------------------------------------------'''

# dic = {
#     'Oi': 'Olá',
#     'Tchau': 'Até mais'
# }

# saudacao = input('Diga Oi ou Tchau: ')
# print(dic[saudacao])

'''--------------------------------------------------'''

# dicionario = {
#     'Professor': ['Danilo', 'Marcel', 'Gabi', 'Leandro', 'Yan'],
#     'Idade': [27, 42, 25, 32, 30],
#     'Carro': ['Celtinha', 'Corola', 'Honda Fit', 'Renegade', 'Golzinho'],
#     'Disciplina': ['Python', 'Matematica', 'SW&TX', 'Storytelling', 'Edge'],
#     'Curso': ['Engenharia de Software', 'Telecom', 'Enfermagem', 'Startups', 'Maromba']
# }

# for key in dicionario.keys():
#     print(dicionario[key])

# professor = input('De quem você quer saber o carro? ')
# for i in range(len(dicionario['Professor'])):
#     if (professor == dicionario['Professor'][i]):
#         index = i
#         break
# print(f"O carro do {professor} é {dicionario['Carro'][index]}")

# professor = input('De quem você quer saber qual a matéria que ensina? ')
# for i in range(len(dicionario['Professor'])):
#     if (professor == dicionario['Professor'][i]):
#         index = i
#         break
# print(f"O carro do {professor} é {dicionario['Carro'][index]}")

'''--------------------------------------------------'''

dicionario = {
    'Professor': ['Danilo', 'Marcel', 'Gabi', 'Leandro', 'Yan'],
    'Idade': [27, 42, 25, 32, 30],
    'Carro': ['Celtinha', 'Corola', 'Honda Fit', 'Renegade', 'Golzinho'],
    'Disciplina': ['Python', 'Matematica', 'SW&TX', 'Storytelling', 'Edge'],
    'Curso': ['Engenharia de Software', 'Telecom', 'Enfermagem', 'Startups', 'Maromba']
}

print(pd.DataFrame(dicionario))
dicionario = pd.DataFrame(dicionario)
dicionario.to_excel('Teste.xlsx')

'''--------------------------------------------------'''

# dicionario = {
#     'Professor': ['Danilo', 'Marcel', 'Gabi', 'Leandro', 'Yan'],
#     'Idade': [27, 42, 25, 32, 30],
#     'Carro': ['Celtinha', 'Corola', 'Honda Fit', 'Renegade', 'Golzinho'],
#     'Disciplina': ['Python', 'Matematica', 'SW&TX', 'Storytelling', 'Edge'],
#     'Curso': ['Engenharia de Software', 'Telecom', 'Enfermagem', 'Startups', 'Maromba']
# }

# for key in dicionario.keys():
#     value = input(f"Digite o {key}: ")
#     dicionario[key].append(value)
                  
# print(dicionario)