listaproduto = []
def exibirMenu():
    print("0 - Atualizar produto")
    print("1 - Cadastrar Produto")
    print("2 - Excluir um produto")
    print("3 - Listar produto")
    print("4 - Sair")
    print("\n")
    opcao = int(input("Digite uma opcao: "))
    return opcao

def atualizarproduto():
    nomeproduto = input("Digite o nome do produto a ser atualizado: ")
    indice = -1
    encontrou = False
    for elemento in listaproduto:
        indice += 1
        if elemento == nomeproduto:
            encontrou = True
            
        if (encontrou):
            del listaproduto[indice]
            novoproduto = input("Digite o novo nome ao produto: ")
            listaproduto.append(novoproduto)
            break
            


def inserirproduto():
    novoproduto = input("Digite o nome do produto: ")
    listaproduto.append(novoproduto)

def listarproduto():
    for elemento in listaproduto:
        print (elemento)

def excluirproduto():
    nomeproduto = input("Digite o nome do produto que deseja excluir:")
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
    elif opcao == 0:
        atualizarproduto()
        print('\n')
