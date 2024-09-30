import pytest 

from atividade.models.engenheiro import Engenheiro
from atividade.models.funcionario import Funcionario 
from atividade.models.endereco import Endereco

@pytest.fixture
def criar_engenheiro():
    engenheiro1 = Engenheiro("crea", Funcionario)
    return engenheiro1

def test_engenheiro_alterar_crea_valido(criar_engenheiro):
    criar_engenheiro.crea = "crea2"
    assert criar_engenheiro.crea == "crea2"

def test_engenheiro_crea_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A CREA deve ser um texto."):
        Engenheiro(2, Funcionario)

def test_engenheiro_crea_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A CREA não deve estar vazio."):
        Engenheiro("", Funcionario)