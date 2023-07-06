from pydantic import BaseModel, field_validator


class Cadastro(BaseModel):
    email: str
    senha_1: str
    senha_2: str

    # Validação default
    @field_validator('email')
    def email_deve_ter_arroba(cls, v):
        # v é o valor passado no load
        if '@' not in v:
            raise ValueError('Não tem @ no email.')
        return v
    
    @field_validator('senha_1', 'senha_2')
    def senha_tem_mais_de_10_chars(cls, v):
        if len(v) <= 10:
            raise ValueError('Senha deve ter mais de 10 caracteres.')
        return v
    
    @field_validator('senha_2')
    def senhas_iguais(cls, v, values):
        if v == values['senha_1']:
            return v
        else:
            raise ValueError('Senhas diferentes.')
