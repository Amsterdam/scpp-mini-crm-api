from api.models.tables import DbEnhancedNote
from sqlalchemy.orm import joinedload


def get_base_query(db):
    result = db.query(
        DbEnhancedNote,
    ).options(
        joinedload(DbEnhancedNote.schools)
    ).options(
        joinedload(DbEnhancedNote.tags)
    ).options(joinedload(DbEnhancedNote.contacts)).order_by(DbEnhancedNote.start.desc())

    return result


def all(db):
    result = get_base_query(db).all()
    return result
