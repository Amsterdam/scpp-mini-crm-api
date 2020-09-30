import json

from .models import DbSchool, DbContact


def get_school_query(db):
    return db.query(
        DbSchool.id,
        DbSchool.naam
    )


def get_contact_query(db):
    return db.query(
        DbContact.id,
        DbContact.naam
    )


def construct_result(schoolresult, contactresult):
    feature_collection = []
    for entry in contactresult:
        out = {
            "avatar": "/data/teacher.svg",
            "id": "school_" + str(entry[0]),
            "name": entry[1],
            "type": "contact"
        }
        feature_collection.append(out)
    for entry in schoolresult:
        out = {
            "avatar": "/data/school.svg",
            "id": "teacher_" + str(entry[0]),
            "name": entry[1],
            "type": "school"
        }
        feature_collection.append(out)
    return feature_collection


def json_search(search, db):
    search_filter = "%{}%".format(search)
    schoolresult = get_school_query(db).filter(DbSchool.naam.ilike(search_filter)).all()
    contactresult = get_contact_query(db).filter(DbContact.naam.ilike(search_filter)).all()
    return construct_result(schoolresult, contactresult)
