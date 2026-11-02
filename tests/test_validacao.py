import pytest
from validacao import validacao_metodo_de_pagamento, validacao_de_tipo


@pytest.mark.parametrize("entrada, esperado", [
    ("1", "Pix/débito"),
    ("2", "Dinheiro"),
    ("3", "Crédito")
])


def test_validacao_metodo_pagamento(monkeypatch, entrada, esperado):
    """"verifica se para cada metodo de pagamento ele retorna o numero desejado"""

    monkeypatch.setattr("builtins.input", lambda _: entrada)

    resultado = validacao_metodo_de_pagamento()
    assert resultado == esperado


@pytest.mark.parametrize("entrada, esperado",
    [("1", "Mercado"), ("2", "Feira do mês"),("3", "Roupas"), ("4", "Parcela"),
    ("5", "Uber"), ("6", "Lanche"), ("7", "Lazer"), ("8", "Remédio")])

def test_validacao_de_tipo(monkeypatch, entrada, esperado):
    """"verifica se para cada categoria ele retorna o numero desejado"""
    monkeypatch.setattr("builtins.input", lambda _: entrada)

    resultado = validacao_de_tipo()
    assert resultado == esperado
