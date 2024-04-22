'''peixes = {
    'Espécies' : ['Tilápia',"Baiacu","Tucunaré","Lambaqui","Salmão","Bacalhau","Truta"],
    'Valor' : [25,30,20,101,45,60,15],
    'Região' : ["Piracicaba","Oceania","Amazonas","aguas raras","Noruega","Portugal","zona leste"],
    'estoque' : [10,23,3,31,42,12,21],
    'validade' : [9,2,10,11,7,6,3]
}
dic = {
    'chave':'valor'
}
#print(dic['valor'])
dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = 'outro valor'
print(dic)
dic['chave'] = [dic['chave']]
print(dic)
dic['chave'].append('dhsifuds')
print(dic)
print(dic.keys())
for key in dic.keys():
    print(f"{key} : {dic[key]}")


frase = "Esta casa está ladrilhada, quem a desenladrilhará? O desenladrilhador. O desenladrilhador que a desenladrilhar, bom desenladrilhador será!"
frase = "Maria-mole é molenga. Se não é molenga, não é maria-mole. É coisa malemolente, nem mala, nem mola, nem Maria, nem mole."
print(frase)
frase = frase.lower()
print(frase)
for char in ',?.!':
    frase = frase.replace(char,'')
print(frase)
frase = frase.split(" ")
print(frase)
palavras = {}
for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
print(palavras)
'''
peixes = {
    'Espécies' : ['Tilápia',"Baiacu","Tucunaré","Lambaqui","Salmão","Bacalhau","Truta"],
    'Valor' : [25,30,20,101,45,60,15],
    'Região' : ["Piracicaba","Oceania","Amazonas","aguas raras","Noruega","Portugal","zona leste"],
    'estoque' : [10,23,3,31,42,12,21],
    'validade' : [9,2,10,11,7,6,3]
}
dicionario_de_indices = {peixes["Espécies"][i] : i for i in range(len(peixes["Espécies"])) }

def forca_opcao(msg,opcoes,msg_erro = None):
    resposta = input(msg)
    while resposta not in opcoes:
        print("Resposta inválida")
        if msg_erro:
            print(msg_erro)
        resposta = input(msg)
    return resposta

def remover():
    peixe = forca_opcao("Qual peixe vc deseja remover?\n"
                    ,peixes['Espécies'],"\n".join(peixes["Espécies"]))
    indice = dicionario_de_indices[peixe]
    for key in peixes.keys():
        peixes[key].pop(indice)
    return

def cadastrar():
    for key in peixes:
        info = input(f"Diga o novo {key}: ")
        peixes[key].append(info)
    return

def atualizar():
    peixe = forca_opcao("Qual peixe vc deseja alterar?\n"
                    ,peixes['Espécies'],"\n".join(peixes["Espécies"]))
    indice = dicionario_de_indices[peixe]
    for key in peixes.keys():
        if key != 'Espécies':
            info = input(f"Diga o novo {key}: ")
            peixes[key][indice] = info
    return

def mostrar():
    peixe = forca_opcao("Qual peixe vc deseja ver?\n"
                    ,peixes['Espécies'],"\n".join(peixes["Espécies"]))
    indice = dicionario_de_indices[peixe]
    for key in peixes.keys():
        print(f"{key} : {peixes[key][indice]}")
    return

def atualiza_indces():
    indices = {peixes["Espécies"][i] : i for i in range(len(peixes["Espécies"])) }
    return indices

def menu():
    global dicionario_de_indices
    acoes = ['Cadastrar','Alterar','Remover','Ler','sair']
    while True:
        acao = forca_opcao("O que vc deseja fazer hoje?",acoes,'\n'.join(acoes))
        if acao == acoes[0]:
            cadastrar()
            dicionario_de_indices = atualiza_indces()
        elif acao == acoes[1]:
            atualizar()
        elif acao == acoes[2]:
            remover()
            dicionario_de_indices = atualiza_indces()
        elif acao == acoes[3]:
            mostrar()
        else:
            print("flw")
            break
menu()
#Remover do estoque
#Cadastro de novo peixe
