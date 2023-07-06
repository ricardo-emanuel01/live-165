from pydantic import validate_call
from typing import Union


@validate_call
def soma(x: int, y: int) -> int:
    return x + y
