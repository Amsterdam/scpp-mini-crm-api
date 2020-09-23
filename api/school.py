import json

from .models import DbSchool


def get_base_query(db):
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
                "name": entry[6],
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


def construct_result(result):
    feature_collection = []
    for entry in result:
        out = {
            "type": "School",
            "id": entry[0],
            "school_id": entry[1],
            "lrkp_id": entry[2],
            "school_type": entry[3],
            "brin": entry[4],
            "vestigingsnummer": entry[5],
            "name": entry[6],
            # "grondslag": entry[7],
            # "schoolwijzer_url": entry[8],
            # "onderwijsconcept": entry[9],
            # "heeft_voorschool": entry[10],
            # "leerlingen": entry[11],
            "address": entry[12],
            # "postcode": entry[13],
            # "suburb": entry[14],
            # "website": entry[15],
            # "email": entry[16],
            # "phone": entry[17],
            # "city": entry[18],
        }
        feature_collection.append(out)
    return feature_collection


def geojson_all(db):
    result = get_base_query(db).all()
    return construct_geojson(result)


def json_all(db):
    result = get_base_query(db).all()
    return construct_result(result)


def json_search(search, db):
    search_filter = "%{}%".format(search)
    result = get_base_query(db).filter(DbSchool.naam.ilike(search_filter)).all()
    return construct_result(result)
