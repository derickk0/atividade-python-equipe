import pytest
from atividade.models.funcionario import Funcionario
from atividade.models.endereco import Endereco

@pytest.fixture
def funcionario_valido():
    funcionario1 = Funcionario("Neymar", "telefone1","email1",Endereco("logradouro", "numero", "complemento", "cep", "cidade"), 5000)
    return funcionario1

# Testando o nome
def test_funcionario_alterar_nome_valido(funcionario_valido):
    funcionario_valido.nome = "Messi"
    assert funcionario_valido.nome == "Messi"

def test_funcionario_nome_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Funcionario(2, "telefone", "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

def test_funcionario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        Funcionario("", "telefone", "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

# Testando o telefone
def test_funcionario_alterar_telefone_valido(funcionario_valido):
    funcionario_valido.telefone = "555"
    assert funcionario_valido.telefone == "555"

def test_funcionario_telefone_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone deve ser um texto."):
        Funcionario("Neymar", 55, "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

def test_funcionario_telefone_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O telefone não deve estar vazio."):
        Funcionario("Neymar", "", "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

# Testando o email
def test_funcionario_alterar_email_valido(funcionario_valido):
    funcionario_valido.email = "ff@gmail"
    assert funcionario_valido.email == "ff@gmail"

def test_funcionario_email_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O E-Mail deve ser um texto."):
        Funcionario("Neymar", "telefone", 99, Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

def test_funcionario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O E-Mail não deve estar vazio."):
        Funcionario("Neymar", "telefone", "", Endereco("logradouy", "numero", "com", "cep", "cidade"), 5000)

# Testando o salário
def test_funcionario_alterar_salario_valido(funcionario_valido):
    funcionario_valido.salarioFinal = 10000
    assert funcionario_valido.salarioFinal == 10000

def test_funcionario_salarioFinal_tipo_invalido_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número."):
        Funcionario("Neymar", "telefone", "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), "20000")

def test_funcinario_salarioFinal_negativo_mensagem_erro():
    with pytest.raises(ValueError, match="O salário deve ser um número positivo."):
        Funcionario("Neymar", "telefone", "email", Endereco("logradouy", "numero", "com", "cep", "cidade"), -3000)