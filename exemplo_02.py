from pydantic.dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


Pessoa(nome='Ricardo', idade=22)
