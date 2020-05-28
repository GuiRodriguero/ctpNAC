import sys
from EntregaXPTO.xpto_funcoes import *

escolha = menu()
isLogado = False

while escolha >= 0 or escolha < 0:

    if escolha == 1:
        cadastrarProduto(informarProduto())

    if escolha == 2:
        alterarProduto()

    if escolha == 3:
        excluirProduto()

    if escolha == 4:
        listaProduto()

    if escolha == 5:
        comprarProduto()

    if escolha == 6:
        venderProduto()

    if escolha == 7:
        sys.exit()

    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6 and escolha != 7:
        print("\nDigite um valor entre 1 e 4\n")

    escolha = menu()
