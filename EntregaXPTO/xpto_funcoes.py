import sys

codigo_produto = []
descricao_produto = []
quantidade_produto = []


def menu():
    opcao = int(input("1 - Cadastrar produto \n"
                        "2 - Alterar produto \n"
                        "3 - Excluir produto \n"
                        "4 - Listar estoque de peças \n"
                        "5 - Comprar produto \n"
                        "6 - Vender produto \n"
                        "7 - Sair  \n"))
    return opcao

def informarProduto():
    codigo = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade deste produto: "))

    return codigo, descricao, quantidade

def cadastrarProduto(produto):

    if produto[0] not in codigo_produto:
        codigo_produto.append(produto[0])
        descricao_produto.append(produto[1])
        quantidade_produto.append(produto[2])

    else:
        print("PRODUTO NÃO CADASTRADO! ESTE CÓDIGO JÁ EXISTE NO SISTEMA\n")

def alterarProduto():
    tentativa = 0

    while tentativa < 3:
            senha_digitada = input("Senha: ")
            if senha_digitada == "yN1825*a":
                produto = acharProduto()

                if produto[0] not in codigo_produto:
                    print("PRODUTO NÃO CADASTRADO\n\n")
                else:
                    descricao = input("Digite a nova descrição do produto: ")
                    quantidade = -1
                    while quantidade < 0:
                        quantidade = int(input("Digite a nova quantidade deste produto: "))

                    descricao_produto[produto[1]] = descricao
                    quantidade_produto[produto[1]] = quantidade
            else:
                print("SENHA INCORRETA")
                tentativa += 1
                if tentativa == 3:
                    print("SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR\n\n")
                    sys.exit()

    tentativa = 4

def excluirProduto():
    tentativa = 0
    while tentativa < 3:
        senha_digitada = input("Senha: ")
        if senha_digitada == "yN1825*a":
            produto = acharProduto()

            if produto[0] not in codigo_produto:
                print("PRODUTO NÃO CADASTRADO\n\n")
            else:
                escolha = input("Deseja excluir o produto? (S/N) ").upper()
                if escolha == "S":
                    del (codigo_produto[produto[1]])
                    del (descricao_produto[produto[1]])
                    del (quantidade_produto[produto[1]])

                    print("PRODUTO EXCLUIDO COM SUCESSO\n\n")
                else:
                    print("PRODUTO NÃO EXCLUÍDO\n")
        else:
            print("SENHA INCORRETA")
            tentativa += 1
            if tentativa == 3:
                print("SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR\n\n")
                sys.exit()

    tentativa = 4


def listaProduto():
    print("CÓDIGO       ", end="")
    print("DESCRIÇÃO    ", end="")
    print("QUANTIDADE EM ESTOQUE")

    for x in range(len(codigo_produto)):
        limite = 0

        print(codigo_produto[x], "          ", descricao_produto[x], "                  ", quantidade_produto[x])

        if quantidade_produto[x] < 100:
            limite += 1

    print("Quantidade de produtos cadastrados: ", len(codigo_produto))
    print("Quantidade de itens em estoque: ", sum(quantidade_produto))
    print("Produtos com estoque abaixo do mínimo permitido (100 unidades): ", limite)

def comprarProduto():

    produto = acharProduto()

    if produto[0] not in codigo_produto:
        print("PRODUTO NÃO CADASTRADO\n\n")

    else:
        pedido = -1
        while pedido < 0:
            pedido = int(input("Digite a quantidade que deseja comprar deste produto: "))

        quantidade_produto[produto[1]] += pedido

def venderProduto():
    produto = acharProduto()

    if produto[0] in codigo_produto:
        pedido = -1
        while pedido < 0:
            pedido = int(input("Digite a quantidade que deseja comprar deste produto: "))

        if pedido < quantidade_produto[produto[1]]:
            quantidade_produto[produto[1]] -= pedido
        else:
            print("VENDA NÃO PERMITIDA. ESTOQUE INSUFICIENTE!\n\n")
    else:
        print("PRODUTO NÃO CADASTRADO\n\n")

def acharProduto():
    codigo = input("Digite o código do produto: ")


    if codigo in codigo_produto:
        posicao = codigo_produto.index(codigo)
        print("Descrição: ", descricao_produto[posicao])
        print("Quantidade: ", quantidade_produto[posicao])

    return codigo