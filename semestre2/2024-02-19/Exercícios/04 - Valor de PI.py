inputText = 'Com quantos termos deseja calcular o valor de PI? '

x = input(inputText)
while (not x.isnumeric()):
    print('Valor inválido!')
    x = input(inputText)
x = int(x)

calc = 0

divisor = 1
sinal = 'pos'
pi = 0

for i in range(x):
    if (sinal == 'pos'):
        pi += 1 / divisor
        sinal = 'neg'
    else:
        pi -= 1 / divisor
        sinal = 'pos'

    divisor += 2

pi *= 4

print(f'O valor de PI utilizando {x} termos é igual a {pi}')
