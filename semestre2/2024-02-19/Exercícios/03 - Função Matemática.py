
inputText = 'Digite um valor: '

x = input(inputText)
while (not x.isnumeric()):
    print('Valor inválido!')
    x = input(inputText)
x = float(x)

if (x <= 2):
    print(f'f(x) = {x}')
elif (x <= 3.5):
    print(f'f(x) = 2')
elif (x <= 5):
    print(f'f(x) = 3')
else:
    print(f'f(x) = {(x*x)-10*x+28}')
