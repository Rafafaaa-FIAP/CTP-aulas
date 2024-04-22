'''
10 - Dados dois dicionários, retorne uma lista com as chaves que não são comuns aos dois.
'''

dic1 = {
  'a': 'a',
  'b': 'b',
  'c': 'c',
}

dic2 = {
  'd': 'd',
  'e': 'e',
  'f': 'f',
}

chaves = []
for key in dic1.keys():
  if (key not in dic2.keys()):
    chaves.append(key)
for key in dic2.keys():
  if (key not in dic1.keys()):
    chaves.append(key)
print(chaves)