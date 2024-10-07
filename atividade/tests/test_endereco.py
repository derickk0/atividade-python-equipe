import pytest
from atividade.models.funcionario import Funcionario
from atividade.models.endereco import Endereco

@pytest.fixture
def endereco_valido():
    endereco1 = Endereco("Rua A.", "44", "N/A", "434", "Salvador")
    return endereco1

# Testar logradouro
def test_endereco_alterar_logradouro_valido(endereco_valido):
    endereco_valido.logradouro = "Rua B."
    assert endereco_valido.logradouro == "Rua B."

def test_enderco_logradouro_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Endereco(2, "44", "N/A", "434", "Salvador")

def test_endereco_logradouro_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O logradouro não deve estar vazio."):
        Endereco("", "44", "N/A", "434", "Salvador")

# Testar numero
def test_endereco_alterar_numero_valido(endereco_valido):
    endereco_valido.numero = "55"
    assert endereco_valido.numero == "55"

def test_endereco_numero_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O numero deve ser um texto."):
        Endereco("Rua A.", 55, "N/A", "434", "Salvador")

def test_endereco_numero_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O numero não deve estar vazio."):
        Endereco("Rua A.", "", "N/A", "434", "Salvador")

# Testar complemento
def test_endereco_alterar_complemento_valido(endereco_valido):
    endereco_valido.complemento= "Bar"
    assert endereco_valido.complemento== "Bar"

def test_enderco_complmento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Endereco("Rua A.", "44", 99, "434", "Salvador")

def test_endereco_complemento_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O complemento não deve estar vazio."):
        Endereco("Rua A.", "44", "", "434", "Salvador")

# Testar cep
def test_endereco_alterar_cep_valido(endereco_valido):
    endereco_valido.cep= "88"
    assert endereco_valido.cep == "88"

def test_enderco_cep_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O cep deve ser um texto."):
        Endereco("Rua A.", "44", "N/A", 88, "Salvador")

def test_endereco_cep_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O cep não deve estar vazio."):
        Endereco("Rua A.", "44", "N/A", "", "Salvador")

# Testar cidade
def test_endereco_alterar_cidade_valido(endereco_valido):
    endereco_valido.cidade = "Bar"
    assert endereco_valido.cidade == "Bar"

def test_enderco_cidade_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Endereco("Rua A.", "44", "N/A", "434", 99)

def test_endereco_cidade_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="A cidade não deve estar vazio."):
        Endereco("Rua A.", "44", "N/A", "434", "")
        
        
        