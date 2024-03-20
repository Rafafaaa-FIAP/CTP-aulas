
demandas = []

while True:
    opcoes_id = ['1','2','3','4']
    opcoes_text = ['Adicionar demanda','Ver demandas','Executar a primeira demanda','Sair']

    inputText = f'Escolha uma opção:'
    for i in range(len(opcoes_id)):
        inputText += f'\n{opcoes_id[i]} - {opcoes_text[i]}'
    inputText += '\n'

    opcao = input(inputText)
    while (opcao not in opcoes_id):
        print('Opção inválida!')
        opcao = input(inputText)
    opcao = int(opcao)

    if (opcao == 1):
        titulo = input('Digite o título da demanda: ')
        demandas.append(titulo)
        print('Demanda adicionada com sucesso!')
    elif (opcao == 2):
        for x in demandas:
            print(x)
    elif (opcao == 3):
        demandas.pop(0)
        print('Demanda executada com sucesso!')
    elif (opcao == 4):
        print('Obrigado por utilizar nossos serviços!')
        break
