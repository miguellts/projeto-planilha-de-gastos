from categorias import categorias, metodos

def validacao_preco():
    """função que solicita e valida o preço, para saber se é um numero"""
    while True:
        try:
            preco = float(input("adicione o preço "))
    
            if (preco <= 0):
                print("preço não pode ser 0 ou menor que 0")
                continue
    
            return preco
    
        except ValueError:
            print("preço inválido! digite um valor numérico")


def validacao_metodo_de_pagamento():
    """função que solicita e valida o metodo de pagamento"""

    for i, metodo in enumerate(metodos, start=1):
        print(f"{i}- {metodo}")
    while True:
        try:
            opcao = int(input("adicione o metodo de pagamento "))

            if(opcao <= 0 or opcao > len(metodos)):
                print("método inválido!")
                continue

            else:
                return metodos[opcao - 1]
            
        except ValueError:
            print("método inválido! digite um valor numérico")

def validacao_de_tipo():
    """função que sollicita e valida  a categoria"""
    for i, categoria in enumerate(categorias, start = 1):
        print(f"{i}- {categoria}")

    while True:
        try:
            opcao = int(input("adicione o tipo de compra "))

            if(opcao <= 0 or opcao > len(categorias)):
                print("categoria inválida!")
                continue
            
            else:
                return categorias[opcao - 1]

        except ValueError:
            print("categoria inválida! digite um número válido")
        
    