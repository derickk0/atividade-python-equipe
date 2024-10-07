from atividade.models.funcionario import Funcionario
class Engenheiro: 
    def __init__(self, crea: str, funcionario: Funcionario) -> None:
        self.crea = self._verificar_crea(crea)
        self.funcionario = funcionario

    # Testar crea
    def _verificar_crea(self, valor):
        self._verificar_crea_tipo_invalido(valor)
        self._verificar_crea_vazio_invalido(valor)

        self.crea = valor 
        return self.crea

    def _verificar_crea_tipo_invalido(self, valor): 
        if not isinstance(valor, str): 
            raise TypeError("A CREA deve ser um texto.")

    def _verificar_crea_vazio_invalido(self, valor): 
        if not valor.strip():
            raise ValueError("A CREA não deve estar vazio.")