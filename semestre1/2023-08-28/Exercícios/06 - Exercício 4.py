'''
4. As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
'''

qtd = int(input('Digite quantas maçãs você irá comprar: '))
valorUni = 0.25
if (qtd < 12):
    valorUni = 0.3
print(f'Valor total da compra é: {round(valorUni * qtd, 2)}')
