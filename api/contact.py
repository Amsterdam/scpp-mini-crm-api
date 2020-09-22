from .models import DbContact


def get_base_query(db):
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


def json_all(db):
    result = get_base_query(db).all()
    return construct_result(result)
