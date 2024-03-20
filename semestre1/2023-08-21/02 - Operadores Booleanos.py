#--> Operadores booleanos
#--> or (retorna True se algum dos booleanos for True)
#--> and (retorna True se todos os booleanos forem True)
contador = 1
num1 = int(input(f'Digite o {contador}º número: '))
contador = contador + 1
num2 = int(input(f'Digite o {contador}º número: '))
contador = contador + 1
num3 = int(input(f'Digite o {contador}º número: '))
contador = contador + 1
num4 = int(input(f'Digite o {contador}º número: '))

print("Comparações com or: ")
print(f"{num1} > {num2} or {num3} < {num4}, ou seja, {num1 > num2} or {num3 < num4} resulta em "
      f"{num1 > num2 or num3 < num4}")
print(f"{num1} > {num2} or {num3} > {num4}, ou seja, {num1 > num2} or {num3 > num4} resulta em "
      f"{num1 > num2 or num3 > num4}")
print(f"{num1} < {num2} or {num3} < {num4}, ou seja, {num1 < num2} or {num3 < num4} resulta em "
      f"{num1 < num2 or num3 < num4}")
print(f"{num1} < {num2} or {num3} > {num4}, ou seja, {num1 < num2} or {num3 > num4} resulta em "
      f"{num1 < num2 or num3 > num4}")
print("Comparações com and: ")
print(f"{num1} > {num2} and {num3} < {num4}, ou seja, {num1 > num2} and {num3 < num4} resulta em "
      f"{num1 > num2 and num3 < num4}")
print(f"{num1} > {num2} and {num3} > {num4}, ou seja, {num1 > num2} and {num3 > num4} resulta em "
      f"{num1 > num2 and num3 > num4}")
print(f"{num1} < {num2} and {num3} < {num4}, ou seja, {num1 < num2} and {num3 < num4} resulta em "
      f"{num1 < num2 and num3 < num4}")
print(f"{num1} < {num2} and {num3} > {num4}, ou seja, {num1 < num2} and {num3 > num4} resulta em "
      f"{num1 < num2 and num3 > num4}")
