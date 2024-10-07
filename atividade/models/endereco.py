class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro )
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)

    # Testar nome
    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    def _verificar_logradouro_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O logradouro não deve estar vazio.")
        
    # Testar numero
    def _verificar_numero(self, valor2):
        self._verificar_numero_tipo_invalido(valor2)
        self._verificar_numero_vazio_invalido(valor2)

        self.numero = valor2
        return self.numero
    
    def _verificar_numero_tipo_invalido(self, valor2):
        if not isinstance(valor2, str):
            raise TypeError("O numero deve ser um texto.")
        
    def _verificar_numero_vazio_invalido(self, valor2):
        if not valor2.strip():
            raise ValueError("O numero não deve estar vazio.")
   
    # Testar complemento
    def _verificar_complemento(self, valor3):
        self._verificar_complemento_tipo_invalido(valor3)
        self._verificar_complemento_vazio_invalido(valor3)

        self.complemento = valor3
        return self.complemento
    
    def _verificar_complemento_tipo_invalido(self, valor3):
        if not isinstance(valor3, str):
            raise TypeError("O complemento deve ser um texto.")
        
    def _verificar_complemento_vazio_invalido(self, valor3):
        if not valor3.strip():
            raise ValueError("O complemento não deve estar vazio.")
   
    # Testar cep
    def _verificar_cep(self, valor4):
        self._verificar_cep_tipo_invalido(valor4)
        self._verificar_cep_vazio_invalido(valor4)

        self.cep = valor4
        return self.cep
    
    def _verificar_cep_tipo_invalido(self, valor4):
        if not isinstance(valor4, str):
            raise TypeError("O cep deve ser um texto.")
        
    def _verificar_cep_vazio_invalido(self, valor4):
        if not valor4.strip():
            raise ValueError("O cep não deve estar vazio.")
  
    # Testar cidade
    def _verificar_cidade(self, valor5):
        self._verificar_cidade_tipo_invalido(valor5)
        self._verificar_cidade_vazio_invalido(valor5)

        self.cidade = valor5
        return self.cidade
    
    def _verificar_cidade_tipo_invalido(self, valor5):
        if not isinstance(valor5, str):
            raise TypeError("A cidade deve ser um texto.")
        
    def _verificar_cidade_vazio_invalido(self, valor5):
        if not valor5.strip():
            raise ValueError("A cidade não deve estar vazio.")
        