from .models.tables import DbContact


def get_base_query(db):
    return db.query(
        DbContact
    )


def by_id(id, db):
    return get_base_query(db).filter(DbContact.id == id).first()


def name_search(search, db):
    search_filter = "%{}%".format(search)
    return get_base_query(db).filter(DbContact.naam.ilike(search_filter)).all()


def phone_search(search, db):
    search_filter = "%{}%".format(search)
    return get_base_query(db).filter(DbContact.phone.ilike(search_filter)).all()


def all(db):
    return get_base_query(db).all()
