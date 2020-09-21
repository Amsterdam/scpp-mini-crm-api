import json
from .models import DbSchool
from .database import SessionLocal, engine
from .settings import settings
from geoalchemy2 import func


def get_base_query():
    db = SessionLocal()
    return db.query(
        DbSchool.id,
        DbSchool.school_id,
        DbSchool.lrkp_id,
        DbSchool.school_type,
        DbSchool.brin,
        DbSchool.vestigingsnummer,
        DbSchool.naam,
        DbSchool.grondslag,
        DbSchool.schoolwijzer_url,
        DbSchool.onderwijsconcept,
        DbSchool.heeft_voorschool,
        DbSchool.leerlingen,
        DbSchool.address,
        DbSchool.postcode,
        DbSchool.suburb,
        DbSchool.website,
        DbSchool.email,
        DbSchool.phone,
        DbSchool.city,
        DbSchool.point.ST_Transform(4326).ST_AsGeoJson())

def construct_geojson(result):
    feature_collection = {
        "type": "FeatureCollection",
        "name": "schools",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": []
    }
    for entry in result:
        out = {
                "type": "Feature",
                "id": entry[0],
                "properties": {
                "school_id": entry[1],
                "lrkp_id": entry[2],
                "school_type": entry[3],
                "brin": entry[4],
                "vestigingsnummer": entry[5],
                "naam": entry[6],
                "grondslag": entry[7],
                "schoolwijzer_url": entry[8],
                "onderwijsconcept": entry[9],
                "heeft_voorschool": entry[10],
                "leerlingen": entry[11],
                "address": entry[12],
                "postcode": entry[13],
                "suburb": entry[14],
                "website": entry[15],
                "email": entry[16],
                "phone": entry[17],
                "city": entry[18],
            },
            "geometry": json.loads(entry[19])
        }
        feature_collection["features"].append(out)
    return feature_collection


def geojson_all():
    
    try:
        result = get_base_query().all()
    except:
        DbSchool.__table__.create(engine)
        result = get_base_query().all()
    return construct_geojson(result)
