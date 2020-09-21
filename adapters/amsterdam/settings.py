import os
from pydantic import HttpUrl, BaseSettings


class Settings(BaseSettings):
    AMSTERDAM_PRIMARY_SCHOOLS = os.environ.get('AMSTERDAM_PRIMARY_SCHOOLS', "https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/po")
    AMSTERDAM_HIGH_SCHOOLS = os.environ.get('AMSTERDAM_HIGH_SCHOOLS', "https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/vo")
    AMSTERDAM_KINDERGARTEN = os.environ.get('AMSTERDAM_KINDERGARTEN', "https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/opvang")
    AMSTERDAM_DAYCARE = os.environ.get('AMSTERDAM_DAYCARE', "https://schoolwijzer.amsterdam.nl/nl/api/v1/lijst/bso")


settings = Settings()
