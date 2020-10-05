from api.models.tables import DbTag, enhanced_note_tag_table
from sqlalchemy import func


def get_base_query(db):
    return db.query(
        DbTag.id,
        DbTag.tag,
        DbTag.type,
        DbTag.description,
        func.count(enhanced_note_tag_table.c['enhanced_note_id'])
    ).join(enhanced_note_tag_table, isouter=True)


def construct_result(result):
    feature_collection = []
    for entry in result:
        feature_collection.append({
            "id": entry[0],
            "tag": entry[1],
            "notes": entry[2]
        })
    return feature_collection


def json_all(db):
    return get_base_query(db).group_by(DbTag.id).order_by(
        func.count('enhanced_note_tag.enhanced_note_id').desc()).all()
