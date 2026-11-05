from compras import Compras

from validacao import definicao_preco, definicao_metodo_de_pagamento, definicao_de_tipo



compras = []
valor_total = 0
numero_de_compras = 0

def executar_menu():
    while True:
        """menu de opçoes"""

        print("\n")
        print("ESCOLHA UMA OPÇÃO")
        print("1 - adicionar compra")
        print("2 - excluir compra")
        print("3 - visualizar gastos")
        print("4 - sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            preco = definicao_preco()
            print("================================")
            tipo = definicao_de_tipo()
            print("================================")
            metodo = definicao_metodo_de_pagamento()

            nova_compra = Compras(tipo, metodo, preco)
            compras.append(nova_compra)

            valor_total += preco
            numero_de_compras += 1

            print("Compra adicionada com sucesso!")

        if opcao == "3":
            for i in range(numero_de_compras):
                print("===================")
                print(f"id: {i+1}")
                print(f"tipo: {compras[i].tipo}")
                print(f"preço: {compras[i].preco}")
                print(f"Total de gastos: {valor_total}")

        if opcao == "4":
            exit()

if __name__ == "__main__":
    executar_menu()


    


print("\tGASTOS DO MES")
print("===============================")
print("TIPO DE COMPRA\tPREÇO\tMÉTODO DE PAGAMENTO")
