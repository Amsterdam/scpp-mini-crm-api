from api.models.tables import DbEnhancedNote
from sqlalchemy.orm import joinedload


def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


def get_base_query(db):
    result = db.query(
        DbEnhancedNote,
    ).options(
        joinedload(DbEnhancedNote.schools)
    ).options(
        joinedload(DbEnhancedNote.tags)
    ).options(joinedload(DbEnhancedNote.contacts))

    return result


def json_all(db):
    result = get_base_query(db).all()
    return result
