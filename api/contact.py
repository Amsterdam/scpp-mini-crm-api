import json
from .models import DbContact, DbSchool
from .database import SessionLocal, engine, Base
from .settings import settings
from geoalchemy2 import func


def get_base_query():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    return db.query(
        DbContact.id,
        DbContact.naam,
        DbContact.email,
        DbContact.phone,
        DbContact.school_id,
    )

def construct_result(result):
    feature_collection = []
    for entry in result:
        out = {
            "type": "Contact",
            "id": entry[0],
            "naam": entry[1],
            "email": entry[2],
            "phone": entry[3],
            "school_id": entry[4]
        }
        feature_collection.append(out)
    return feature_collection


def json_all():
    result = get_base_query().all()
    return construct_result(result)
