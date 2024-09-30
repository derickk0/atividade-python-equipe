import pytest 

from atividade.models.medico import Medico
from atividade.models.funcionario import Funcionario 
from atividade.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    medico1 = Medico("crm", Funcionario)
    return medico1

def test_medico_alterar_crm_valido(medico_valido):
    medico_valido.crm = "crm2"
    assert medico_valido.crm == "crm2"

def test_medico_crm_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CRM deve ser um texto."):
        Medico(3, Funcionario)

def test_medico_crm_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O CRM não deve estar vazio."):
        Medico("", Funcionario)