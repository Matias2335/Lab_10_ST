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


def test_cupom_dez_abaixo_do_minimo_nao_desconta():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 5000


def test_cupom_desconhecido_e_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


def test_cupom_aplicado_antes_do_item_abaixo_do_minimo():
    carrinho = Carrinho()
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(1000)
    assert carrinho.total == 1000


def test_cupom_dez_vale_no_minimo():
    carrinho = Carrinho()
    carrinho.adicionar(10000)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 9000


def test_cupom_dez_um_abaixo_do_minimo_nao_desconta():
    carrinho = Carrinho()
    carrinho.adicionar(9999)
    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 9999


def test_cupom_aplicado_antes_vale_quando_subtotal_chega_ao_minimo():
    carrinho = Carrinho()
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(10000)
    assert carrinho.total == 9000


def test_cupom_vinte_vale_a_partir_de_30000():
    carrinho = Carrinho()
    carrinho.adicionar(30000)
    carrinho.aplicar_cupom("VINTE")
    assert carrinho.total == 24000


def test_cupom_vinte_abaixo_de_30000_nao_desconta():
    carrinho = Carrinho()
    carrinho.adicionar(29999)
    carrinho.aplicar_cupom("VINTE")
    assert carrinho.total == 29999
