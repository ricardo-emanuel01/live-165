# [Pydantic](https://docs.pydantic.dev/latest/)

Pydantic é uma biblioteca para validação de dados (serialização) e gerenciamento de configurações.

- Validação de dados;
- Data Classes;
- Validação de argumentos de funções.

## Roteiro

1. O que é?
2. Dataclasses
3. Modelos
4. Validadores
5. Campos
6. Modelos de configuração

## Opções ao Pydantic

- Attrs;
- Valideer;
- Marshmellow;
- Django Rest Framework;
- Cerberus.

Essas bibliotecas fazem totalmente ou parcialmente o que o Pydantic se propões a fazer.

- Validando em tempo de execução

```python
from pydantic import validate_arguments


@validate_arguments
def soma(x: int, y: int) -> int:
    return x + y

```

Os validadores são dividos em 3 grupos:

- Default --> Validação durante o carregamento;
- Pré --> Validação antes do carregamento;
- Por item --> Validação de containers (lista, tupla, dict);

**Mudou muita coisa desde a live 17/05/2021**
