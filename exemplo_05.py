from pydantic import BaseModel, field_validator


class Pedidos(BaseModel):
    ids: list[int]

    # Pré validação
    # @field_validator('ids', mode='before')
    # def converter_ids_em_list(cls, v):
    #     return v.split('|')

    # Não funciona!
    @field_validator('ids', each_item=True)
    def converter_ids_em_list(cls, v):
        if v < 0:
            raise ValueError('')
        return v
    
"""
ids = '1|2|3|4|5|6'
Pedidos(**ids)
"""
