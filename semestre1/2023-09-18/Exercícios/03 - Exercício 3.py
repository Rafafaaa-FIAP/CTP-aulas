'''
3 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

popA = 80000
taxaA = 1.03
popB = 200000
taxaB = 1.015
qtdAno = 0
while (popA < popB):
  popA *= taxaA
  popB *= taxaB
  qtdAno += 1
print(f'Depois de {qtdAno} anos a populção do país A ultrapassará ou igualará com a população do país B!')