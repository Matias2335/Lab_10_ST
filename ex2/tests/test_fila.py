import pytest
from fila import Fila

def test_fila_nova_nao_tem_senhas_aguardando():
    assert Fila().aguardando == 0

def test_emitir_normal_devolve_n1():
    assert Fila().emitir("normal") == "N1"