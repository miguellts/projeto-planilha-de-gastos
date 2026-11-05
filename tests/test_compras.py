from compras import Compras

def test_criar_compra():
    """verifica se uma compra é criada com os atributos esperados"""
    compra = Compras("Mercado", "Pix", 50.0)

    assert compra.tipo == "Mercado"
    assert compra.metodo_pagamento == "Pix"
    assert compra.preco == 50.0