from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class MinhaConfig(BaseSettings):
    model_config: dict = SettingsConfigDict(env_prefix='test_')
    mongo_url: str
    postgres_url: PostgresDsn

"""
$ TEST_POSTGRES_URL='postgres://user:password@localhost:5050' TEST_MONGO_URL='asd' ipython -i exemplo_07.py
"""

exemplo = MinhaConfig()
