'''
1 - Modifique o seguinte Código para eliminar o uso de condicionais

Resp = input(“Diga oi ou tchau”)
if resp == ‘oi’:
  Print(“olá”)
else:
  Print(“falou”)
'''

dic = {
  'oi': 'olá',
  'tchau': 'falou'
}

resp = input('Diga oi ou tchau:')
print(dic[resp])
