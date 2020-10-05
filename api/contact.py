from .models.tables import DbContact


def get_base_query(db):
    return db.query(
        DbContact
    )


def construct_result(result):
    feature_collection = []

    for entry in result:
        out = {
            "type": "Contact",
            "id": entry[0],
            "name": entry[1],
            "email": entry[2],
            "phone": entry[3],
            "school_id": entry[4]
        }
        feature_collection.append(out)

    return feature_collection


def json_by_id(id, db):
    return get_base_query(db).filter(DbContact.id == id).first()


def json_search(search, db):
    search_filter = "%{}%".format(search)
    return get_base_query(db).filter(DbContact.naam.ilike(search_filter)).all()


def json_all(db):
    return get_base_query(db).all()
