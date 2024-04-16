'''import requests
peixes = {
    'Espécies' : ['Tilápia',"Baiacu","Tucunaré","Lambaqui","Salmão","Bacalhau","Truta"],
    'Valor' : [25,30,20,101,45,60,15],
    'Região' : ["Piracicaba","Oceania","Amazonas","aguas raras","Noruega","Portugal","zona leste"],
    'estoque' : [10,23,3,31,42,12,21],
    'validade' : [9,2,10,11,7,6,3]
}
compra = {
    "Valor" : 0,
    "Endereço" : {},
    "Peixes" : {}
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
def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
def verifica_numero(msg):
    num = input(msg)
    if not num.isnumeric():
        print("Deve ser um numero inteiro: ")
        num = verifica_numero(msg)
    return int(num)
def comprar():
    opcoes = peixes['Espécies']
    frase = '\n'.join(opcoes)
    sim_nao = ['sim','não']
    s_n = '/'.join(sim_nao)
    while True:
        escolha = forca_opcao(f"Bem vindx à peixaria AGNELLON.\nEssas são"
                              f" as nossas opções de peixes :\n{frase}: ",opcoes,frase)
        local = dicionario_de_indices[escolha]
        qtd = verifica_numero("Quantos kg você deseja levar? ")
        if peixes["estoque"][local] < qtd:
            print("Não temos essa disponibilidade!!!")
            resposta = forca_opcao(f"Voce quer ver outras opções? \n{s_n}: ",sim_nao,s_n)
            if resposta == 'não':
                print("Que pena!!")
                if compra['Valor'] != 0:
                    print("Obrigado por comprar conosco, esse é o resumo da sua compra:")
                    printa_dicionario(compra)
                break
            continue
        else:
            compra['Valor'] += qtd*peixes["Valor"][local]
            if escolha not in compra["Peixes"].keys():
                compra['Peixes'][escolha] = qtd
            else:
                compra['Peixes'][escolha] += qtd
            peixes['estoque'][local] -= qtd
        sair = forca_opcao(f"Você deseja continuar comprando? {s_n}: ",sim_nao,s_n)
        if sair == 'não':
            print("Obrigado por comprar conosco, esse é o resumo da sua compra:")
            printa_dicionario(compra)
            break
    return



def menu_funcionario():
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
def pega_endereco():
    cep = input("Diga seu cep: ")
    endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    while endereco.status_code != 200 or 'erro' in endereco.json().keys():
        print("Diga um cep válido!")
        cep = input("Diga seu cep: ")
        endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    endereco = endereco.json()
    endereco["Nº"] = input("Diga o numero da moradia: ")
    compra["Endereço"] = endereco
    return
while True:
    opcoes = ['cliente','funcionário','s']
    print("Seja Bem vindo à peixaria.")
    resp = forca_opcao("Você é cliente ou funcionário? (s para sair) ",opcoes,'\n'.join(opcoes))
    if resp == 'cliente':
        pega_endereco()
        comprar()
        if compra['Valor'] != 0:
            break
    elif resp == 'funcionário':
        menu_funcionario()
    else:
        print("Tchau")
        break



import requests
cidade = input("Diga uma cidade: ")
url = f"https://open-weather13.p.rapidapi.com/city/{cidade}/PT_BR"

headers = {
	"X-RapidAPI-Key": "42549a053bmsh5baaad1b4f3beb1p1d1281jsn1d0618a3a7ef",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
'''
def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
import requests

url = "https://pokemon-api3.p.rapidapi.com/pokemon"

querystring = {"name":"charmander"}

headers = {
	"X-RapidAPI-Key": "42549a053bmsh5baaad1b4f3beb1p1d1281jsn1d0618a3a7ef",
	"X-RapidAPI-Host": "pokemon-api3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

printa_dicionario(response.json())
