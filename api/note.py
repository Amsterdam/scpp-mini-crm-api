from .models.tables import DbNote


def get_base_query(db):
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
            "contact_id": entry[2]
        }
        feature_collection.append(out)
    return feature_collection


def json_all(db):
    result = get_base_query(db).all()
    return construct_result(result)


def json_by_contact_id(contact_id, db):
    result = get_base_query(db).filter(DbNote.contact_id == contact_id).all()
    return construct_result(result)
