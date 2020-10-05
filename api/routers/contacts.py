from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api.models.tables import DbContact
from api.models.create import Contact, ContactCreate
from api.models.response import ContactResponse
from api import contact

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/contacts", response_model=List[ContactResponse], response_model_exclude_none=True)
def get_all_contacts(db: Session = Depends(get_db)):
    return contact.json_all(db)


@router.get("/api/v1/contacts/{search}", response_model=List[ContactResponse])
def searh_for_contacts(search, db: Session = Depends(get_db)):
    return contact.json_search(search, db)


@router.get("/api/v1/contact/{id}", response_model=ContactResponse)
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
