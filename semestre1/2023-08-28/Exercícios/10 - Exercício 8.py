'''
8. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
  - Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO
  - Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
'''

qtd = int(input('Digite a quantidade de lados de um polígono regular: '))
tipo = 'POLÍGONO NÃO IDENTIFICADO'
if (qtd < 3):
    tipo = 'NÃO É UM POLÍGONO'
elif (qtd == 3):
    tipo = 'TRIÂNGULO'
elif (qtd == 4):
    tipo = 'QUADRADO'
elif (qtd == 5):
    tipo = 'PENTÁGONO'
print(tipo)
