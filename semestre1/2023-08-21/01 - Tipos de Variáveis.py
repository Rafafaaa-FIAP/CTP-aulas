#print(type('Hello World'))

#frase = 'Hello World'
#print(frase)

#frase = 'Hello' + ' ' + 'World'
#print(frase)

'''--------------------------------------------------'''

#--> Desse modo o que o usuário digitar será uma string
# num1 = input('Diga um número: ')
# print(num1)
# num2 = input('Diga outro número: ')
# print(num2)
# print(num1 + num2)

#--> Desse modo o que o usuário digitar será um int
# num1 = int(input('Diga um número: '))
# print(num1)
# num2 = int(input('Diga outro número: '))
# print(num2)
# print(num1 + num2)

'''--------------------------------------------------'''

#--> Usuário digita dois números para calcular operações
# num1 = int(input('Diga um número: '))
# print(num1)
# num2 = int(input('Diga outro número: '))
# print(num2)
# 
# soma = num1 + num2
# subt = num1 - num2
# mult = num1 * num2
# divi = num1 / num2
# rest = num1 % num2
# inte = num1 // num2
# 
# print(f'A soma entre {num1} e {num2} é: {soma}')
# print(f'A subtração entre {num1} e {num2} é: {subt}')
# print(f'A multiplicação entre {num1} e {num2} é: {mult}')
# print(f'A divisão entre {num1} e {num2} é: {divi}')
# print(f'O resto da divisão entre {num1} e {num2} é: {rest}')
# print(f'A parte inteira da divisão entre {num1} e {num2} é: {inte}')

'''--------------------------------------------------'''

#--> Trocar os valores das variáveis entre si
#--> Com lógica
# a = 2
# b = 3
# aux = 0
# print(f'a:{a}', f'b:{b}')
# 
# aux = a
# a = b
# b = aux
# print(f'a:{a}', f'b:{b}')

#--> Com Python
# a = 2
# b = 3
# print(f'a:{a}', f'b:{b}')
# 
# a, b = b, a
# print(f'a:{a}', f'b:{b}')

'''--------------------------------------------------'''

#--> Variáveis acumuladoras
#--> Utilizadas para uma variável não ser subtituida por um novo valor
# frase = 'Hello'
# print(frase)
# frase = 'World'
# print(frase)
# 
# frase = 'Hello'
# frase = frase + ' World'
# print(frase)

#--> Utilizando variáveis acumuladoras com o que o usuário digita
# contador = 1
# frase = ''
# 
# palavra = input(f'Digite a {contador}ª palavra: ')
# frase = frase + ' ' + palavra
# contador = contador + 1
# print(frase)
# palavra = input(f'Digite a {contador}ª palavra: ')
# frase = frase + ' ' + palavra
# contador = contador + 1
# print(frase)
# palavra = input(f'Digite a {contador}ª palavra: ')
# frase = frase + ' ' + palavra
# contador = contador + 1
# print(frase)
# palavra = input(f'Digite a {contador}ª palavra: ')
# frase = frase + ' ' + palavra
# contador = contador + 1
# print(frase)

'''--------------------------------------------------'''

#--> Variáveis booleanas
# var1 = True
# var2 = False
# var3 = 2 < 3
# print(type(var1))
# print(type(var2))
# print(type(var3))

#--> Utilizando variáveis booleanas com o que o usuário digita
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# print(f"A comparação {num1} > {num2} resulta em {num1 > num2}")
# print(f"A comparação {num1} >= {num2} resulta em {num1 >= num2}")
# print(f"A comparação {num1} < {num2} resulta em {num1 < num2}")
# print(f"A comparação {num1} <= {num2} resulta em {num1 <= num2}")
# print(f"A comparação {num1} == {num2} resulta em {num1 == num2}")
# print(f"A comparação {num1} != {num2} resulta em {num1 != num2}")
