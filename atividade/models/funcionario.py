from atividade.models.endereco import Endereco

class Funcionario:
    def __init__(self, nome: str, telefone:str, email:str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco
    
    # Testar nome
    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def _verificar_nome_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O nome não deve estar vazio.")
        
    # Testar telefone
    def _verificar_telefone(self, valor2):
        self._verificar_telefone_tipo_invalido(valor2)
        self._verificar_telefone_vazio_invalido(valor2)

        self.telefone = valor2
        return self.telefone
    
    def _verificar_telefone_tipo_invalido(self, valor2):
        if not isinstance(valor2, str):
            raise TypeError("O telefone deve ser um texto.")
        
    def _verificar_telefone_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O telefone não deve estar vazio.")
    
    # Testar Email
    def _verificar_email(self, valor3):
        self._verificar_email_tipo_invalido(valor3)
        self._verificar_email_vazio_invalido(valor3)

        self.email = valor3
        return self.email
    
    def _verificar_email_tipo_invalido(self, valor3):
        if not isinstance(valor3, str):
            raise TypeError("O E-Mail deve ser um texto.")
        
    def _verificar_email_vazio_invalido(self, valor3):
        if not valor3.strip():
            raise ValueError("O E-Mail não deve estar vazio.")