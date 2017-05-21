listaproduto = []
def exibirMenu():
    print("1 - Cadastrar Produto")
    print("2 - Excluir um produto")
    print("3 - Listar produto")
    print("4 - Sair")
    opcao = int(input("Digite uma opcao: "))
    return opcao

def inserirproduto():
    novoproduto = input("Digite o nome do produto: ")
    listaproduto.append(novoproduto)

def listarproduto():
    for elemento in listaproduto:
        print (elemento)

def excluirproduto():
    nomeproduto = input("Nome do CD que deseja excluir:")
    indice = -1
    encontrou = False
    for elemento in listaproduto:
        indice += 1
        if elemento == nomeproduto:
            encontrou = True
            break
    if (encontrou):
        del listaproduto[indice]

while True:
    print('\n')
    opcao = exibirMenu()
    if opcao == 4:
        break
    elif opcao == 3:
        listarproduto()
    elif opcao == 1:
        inserirproduto()
    elif opcao == 2:
        excluirproduto()
        print('\n')
