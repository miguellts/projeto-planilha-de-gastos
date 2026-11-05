import pytest
from validacao import definicao_metodo_de_pagamento, definicao_de_tipo, excluir_compra
from compras import Compras


@pytest.mark.parametrize("entrada, esperado", [
    ("1", "Pix/débito"),
    ("2", "Dinheiro"),
    ("3", "Crédito")
])


def test_definicao_metodo_pagamento(monkeypatch, entrada, esperado):
    """"verifica se para cada metodo de pagamento ele retorna o numero desejado"""

    monkeypatch.setattr("builtins.input", lambda _: entrada)

    resultado = definicao_metodo_de_pagamento()
    assert resultado == esperado


@pytest.mark.parametrize("entrada, esperado",
    [("1", "Mercado"), ("2", "Feira do mês"),("3", "Roupas"), ("4", "Parcela"),
    ("5", "Uber"), ("6", "Lanche"), ("7", "Lazer"), ("8", "Remédio")])

def test_validacao_de_tipo(monkeypatch, entrada, esperado):
    """"verifica se para cada categoria ele retorna o numero desejado"""
    monkeypatch.setattr("builtins.input", lambda _: entrada)

    resultado = definicao_de_tipo()
    assert resultado == esperado

def test_excluir_compra(monkeypatch):
            
    temp = [Compras("Uber", "Cartão", 20.0)]
    monkeypatch.setattr("builtins.input", lambda _: "1")
    excluir_compra(temp)
           
            
    resultado = len(temp)
    assert resultado == 0
