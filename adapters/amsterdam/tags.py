from .settings import settings
from sqlalchemy.exc import IntegrityError
import json
import urllib.request
from api.database import SessionLocal, engine
from api.models.tables import DbTag
from geoalchemy2 import functions


def run_tags():
    """
    Adapter to insert default tags for the city of Amsterdam
    """
    db = SessionLocal()
    tags = [
        {
            "tag": "parkeervergunning",
            "type": "default",
            "description": "Parkeervergunning (PVG)"
        },
{
            "tag": "wonen",
            "type": "default",
            "description": "Wonen (W)"
        },
        {
            "tag": "reiskostenvergoeding",
            "type": "default",
            "description": "Reiskostenvergoeding (RKV)"
        },
        {
            "tag": "administratie",
            "type": "default",
            "description": "Administratie (A)"
        },
        {
            "tag": "bestuur",
            "type": "default",
            "description": "Bestuur (B)"
        },
        {
            "tag": "directie",
            "type": "default",
            "description": "Directie (D)"
        },
        {
            "tag": "leraren",
            "type": "default",
            "description": "Leraren (L)"
        },
    ]
 
    for entry in tags:
        try:
            row = DbTag(
                tag = entry["tag"],
                type = entry["type"],
                description = entry["description"],
            )
            db.merge(row)
            db.commit()
        except IntegrityError as err:
            print("Error: {0}" .format(err))
            db.rollback()
            pass
    

def run():
    run_tags()
