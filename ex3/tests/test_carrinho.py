import pytest
from carrinho import Carrinho


def test_carrinho_vazio_vale_zero():
    assert Carrinho().total == 0


def test_um_item_de_2500():
    carrinho = Carrinho()
    carrinho.adicionar(2500)
    assert carrinho.total == 2500


def test_quantidade_2_dobra_o_valor():
    carrinho = Carrinho()
    carrinho.adicionar(2500, quantidade=2)
    assert carrinho.total == 5000


def test_preco_zero_e_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)


def test_cupom_dez_em_5000_da_4500():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 4500


def test_cupom_desconhecido_e_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


def test_cupom_aplicado_antes_do_item():
    carrinho = Carrinho()
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(1000)
    assert carrinho.total == 900
