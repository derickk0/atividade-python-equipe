from atividade.models.funcionario import Funcionario

class Medico:
    def __init__(self, crm:str, funcionario: Funcionario) -> None:
        self.crm = self._verificar_crm(crm)
        self.funcionario = funcionario
    
    def _verificar_crm(self, valor):
        self._verificar_crm_tipo_invalido(valor)
        self._verificar_crm_vazio_invalido(valor)

        self.crm = valor
        return self.crm
    
    def _verificar_crm_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser um texto.")
        
    def _verificar_crm_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O CRM não deve estar vazio.")