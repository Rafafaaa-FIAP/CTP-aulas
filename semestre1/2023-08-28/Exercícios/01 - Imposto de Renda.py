'''
Escreva um programa para ler o sálario de uma pessoa e calcule o imposto de renda dessa pessoa.
'''

salario = float(input('Digite o valor do seu salário: '))
aliq = 0
parcela = 0
if (salario <= 2112):
    aliq = 0
    parcela = 0
elif (salario <= 2826.65):
    aliq = 0.075
    parcela = 158.4
elif (salario <= 3751.05):
    aliq = 0.15
    parcela = 370.4
elif (salario <= 4664.68):
    aliq = 0.225
    parcela = 651.73
else:
    aliq = 0.275
    parcela = 884.96
print(f'O valor do seu imposto de renda é de R$ {(salario * aliq) + parcela}')
