import pytest
from fila import Fila

def test_fila_nova_nao_tem_senhas_aguardando():
    assert Fila().aguardando == 0

def test_emitir_normal_devolve_n1():
    assert Fila().emitir("normal") == "N1"
def test_normais_sao_numeradas_em_sequencia():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.emitir("normal") == "N2"
def test_prioritaria_tem_numeracao_propria():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.emitir("prioritaria") == "P1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("prioritaria") == "P2"

def test_tipo_invalido_lanca_value_error():
    with pytest.raises(ValueError):
        Fila().emitir("vip")

def test_emitir_aumenta_aguardando():
    fila = Fila()
    fila.emitir("normal")
    fila.emitir("prioritaria")
    assert fila.aguardando == 2

def test_chamar_fila_vazia_lanca_index_error():
    with pytest.raises(IndexError):
        Fila().chamar()
def test_chamar_devolve_a_senha_e_reduz_aguardando():
    fila = Fila()
    fila.emitir("normal")
    assert fila.chamar() == "N1"
    assert fila.aguardando == 0
def test_normais_sao_chamadas_na_ordem_de_chegada():
    fila = Fila()
    fila.emitir("normal")
    fila.emitir("normal")
    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"
def test_prioritaria_passa_na_frente():
    fila = Fila()
    fila.emitir("normal")
    fila.emitir("prioritaria")
    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
def test_prioritarias_sao_chamadas_na_ordem_de_chegada():
    fila = Fila()
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
def test_apos_duas_prioritarias_chama_normal_se_houver():
    fila = Fila()
    fila.emitir("normal")
    for _ in range(3):
        fila.emitir("prioritaria")
    assert [fila.chamar() for _ in range(4)] == ["P1", "P2", "N1", "P3"]

def test_limite_de_duas_nao_vale_sem_normal_esperando():
    fila = Fila()
    for _ in range(3):
        fila.emitir("prioritaria")
    assert [fila.chamar() for _ in range(3)] == ["P1", "P2", "P3"]
def test_contagem_de_prioritarias_zera_apos_chamar_normal():
        fila = Fila()
        for _ in range(2):
            fila.emitir("normal")
        for _ in range(4):
            fila.emitir("prioritaria")
        esperado = ["P1", "P2", "N1", "P3", "P4", "N2"]
        assert [fila.chamar() for _ in range(6)] == esperado