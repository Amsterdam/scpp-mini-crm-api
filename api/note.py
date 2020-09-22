import json
from .models import DbNote
from .database import SessionLocal, engine
from .settings import settings
from geoalchemy2 import func


def get_base_query():
    db = SessionLocal()
    return db.query(
        DbNote.id,
        DbNote.note,
        DbNote.contact_id,
    )

def construct_result(result):
    feature_collection = []
    for entry in result:
        out = {
            "type": "Note",
            "id": entry[0],
            "note": entry[1],
            "contact_id": entry[4]
        }
        feature_collection.append(out)
    return feature_collection


def geojson_all():
    
    try:
        result = get_base_query().all()
    except:
        DbNote.__table__.create(engine)
        result = get_base_query().all()
    return construct_result(result)
