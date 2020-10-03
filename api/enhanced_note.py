from .models import DbEnhancedNote


def get_base_query(db):
    return db.query(
        DbEnhancedNote.id,
        DbEnhancedNote.note,
        DbEnhancedNote.start,
        DbEnhancedNote.end
    )


def construct_result(result):
    feature_collection = []
    for entry in result:
        out = {
            "type": "Note",
            "id": entry[0],
            "note": entry[1],
            "start": entry[2],
            "end": entry[3]
        }
        feature_collection.append(out)
    return feature_collection

def json_all(db):
    result = get_base_query(db).all()
    return construct_result(result)
