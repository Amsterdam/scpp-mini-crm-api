from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api.models import Contact, ContactCreate, DbContact
from api import contact

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/contacts")
def get_all_contacts(db: Session = Depends(get_db)):
    return contact.json_all(db)


@router.get("/api/v1/contacts/{search}")
def searh_for_contacts(search, db: Session = Depends(get_db)):
    return contact.json_search(search, db)


@router.get("/api/v1/contact/{id}")
def get_contact_by_id(id, db: Session = Depends(get_db)):
    return contact.json_by_id(id, db)


@router.post("/api/v1/contact")
async def post_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if contact.school_id and contact.school_id > 0:
        Contact = DbContact(naam=contact.name, email=contact.email,
                            phone=contact.phone, school_id=contact.school_id)
    else:
        Contact = DbContact(naam=contact.name,
                            email=contact.email, phone=contact.phone)
    db.add(Contact)
    try:
        db.commit()
        db.refresh(Contact)
    except IntegrityError:
        raise HTTPException(
            status_code=500, detail="Duplicate Contact, did you mean to update?")
    return Contact
