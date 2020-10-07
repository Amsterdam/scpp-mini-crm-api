from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy import exc
from sqlalchemy.orm import Session
from api.models.tables import DbContact
from api.models.create import Contact, ContactCreate
from api.models.response import ContactResponse
from api import contact

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/contacts", response_model=List[ContactResponse], response_model_exclude_none=True, response_model_by_alias=False)
def get_all_contacts(db: Session = Depends(get_db)):
    return contact.all(db)


@router.get("/api/v1/contacts/{search}", response_model=List[ContactResponse], response_model_exclude_none=True, response_model_by_alias=False)
def searh_for_contacts(search, db: Session = Depends(get_db)):
    return contact.name_search(search, db)


@router.get("/api/v2/phone/{search}", response_model=List[ContactResponse], response_model_exclude_none=True, response_model_by_alias=False)
def searh_contacts_by_phone_number(search, db: Session = Depends(get_db)):
    return contact.phone_search(search, db)


@router.get("/api/v1/contact/{id}", response_model=ContactResponse, response_model_exclude_none=True, response_model_by_alias=False)
def get_contact_by_id(id, db: Session = Depends(get_db)):
    return contact.by_id(id, db)


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
    except exc.IntegrityError:
        raise HTTPException(
            status_code=400, detail="contact exists: %s" % contact.name)
    return Contact
