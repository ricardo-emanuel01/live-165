from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str
    idade: int


class Pessoas(BaseModel):
    pessoas: list[Pessoa]


class Festa(BaseModel):
    maiores: Pessoas
    menores: Pessoas = []


"""
d = {
    'maiores': {
        'pessoas': [
            {'nome': 'Ricardo', 'idade': 21},
            {'nome': 'Mariana', 'idade': 20}
        ]
    }
}

Festa(**d)

"""
