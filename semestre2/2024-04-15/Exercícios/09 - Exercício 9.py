'''
9 - Dados dois dicionários, retorne uma lista com todas as chaves presentes em ambos.
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
  if (key in dic2.keys()):
    chaves.append(key)
print(chaves)