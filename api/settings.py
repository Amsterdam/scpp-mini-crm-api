import os
from typing import List, Union
import json

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgresql://postgres:postgres@localhost/postgres")
    BACKEND_CORS_ORIGINS_CSV = ""
    #BACKEND_CORS_ORIGINS_CSV: List[AnyHttpUrl] = json.dumps([x.strip() for x in os.environ.get('BACKEND_CORS_ORIGINS_CSV', "http://localhost,http://localhost:4200,http://localhost:3000").split(',')])

    #@validator("BACKEND_CORS_ORIGINS_CSV", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
