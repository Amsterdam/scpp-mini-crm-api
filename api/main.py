from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from . import school, contact, note
from .database import SessionLocal, engine, Base
from .settings import settings
from .models import Contact, ContactCreate, DbContact, Note, NoteCreate, DbNote

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/schools.geojson")
def get_schools_geojson(db: Session = Depends(get_db)):
    return school.geojson_all(db)


@app.get("/api/v1/schools")
def get_schools_json(db: Session = Depends(get_db)):
    return school.json_all(db)


@app.get("/api/v1/schools/{search}")
def get_schools_search_json(search, db: Session = Depends(get_db)):
    return school.json_search(search, db)


@app.get("/api/v1/contacts")
def get_contacts(db: Session = Depends(get_db)):
    return contact.json_all(db)


@app.get("/api/v1/contacts/{search}")
def get_contacts_search_json(search, db: Session = Depends(get_db)):
    return contact.json_search(search, db)


@app.get("/api/v1/contact/{id}")
def get_contact(id, db: Session = Depends(get_db)):
    return contact.json_by_id(id, db)


@app.post("/api/v1/contact")
async def post_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if contact.school_id > 0:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone, school_id=contact.school_id)
    else:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone)
    db.add(Contact)
    db.commit()
    db.refresh(Contact)
    return Contact


@app.get("/api/v1/notes/{contact_id}")
def get_notes(contact_id, db: Session = Depends(get_db)):
    return note.json_by_contact_id(contact_id, db)


@app.post("/api/v1/note")
async def post_note(note: NoteCreate, db: Session = Depends(get_db)):
    Note = DbNote(note=note.note, contact_id=note.contact_id)
    db.add(Note)
    db.commit()
    db.refresh(Note)
    return Note
