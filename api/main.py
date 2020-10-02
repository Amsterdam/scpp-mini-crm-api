from fastapi import Depends, FastAPI, Request, Response, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from . import school, contact, note, search
from .database import SessionLocal, engine, Base
from .settings import settings
from .models import Contact, ContactCreate, DbContact, Note, NoteCreate, DbNote, EnhancedNoteCreate, DbEnhancedNote, DbTag

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
def get_all_schools_in_geojson_format(db: Session = Depends(get_db)):
    return school.geojson_all(db)


@app.get("/api/v1/schools")
def get_all_schools(db: Session = Depends(get_db)):
    return school.json_all(db)


@app.get("/api/v1/schools/{search}")
def search_for_schools(search, db: Session = Depends(get_db)):
    return school.json_search(search, db)


@app.get("/api/v1/contacts")
def get_all_contacts(db: Session = Depends(get_db)):
    return contact.json_all(db)


@app.get("/api/v1/contacts/{search}")
def searh_for_contacts(search, db: Session = Depends(get_db)):
    return contact.json_search(search, db)


@app.get("/api/v1/contact/{id}")
def get_contact_by_id(id, db: Session = Depends(get_db)):
    return contact.json_by_id(id, db)


@app.post("/api/v1/contact")
async def post_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if contact.school_id and contact.school_id > 0:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone, school_id=contact.school_id)
    else:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone)
    db.add(Contact)
    try:
        db.commit()
        db.refresh(Contact)
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Duplicate Contact, did you mean to update?")
    return Contact


@app.get("/api/v1/notes")
def get_all_notes(db: Session = Depends(get_db)):
    return note.json_all(db)


@app.get("/api/v1/notes/{contact_id}")
def get_notes_by_contact_id(contact_id, db: Session = Depends(get_db)):
    return note.json_by_contact_id(contact_id, db)


@app.post("/api/v1/note")
async def post_note(note: NoteCreate, db: Session = Depends(get_db)):
    Note = DbNote(note=note.note, contact_id=note.contact_id)
    db.add(Note)
    db.commit()
    db.refresh(Note)
    return Note


@app.post("/api/v2/note")
async def post_enhanced_note(note: EnhancedNoteCreate, db: Session = Depends(get_db)):
    Note = DbEnhancedNote(note=note.note, start=note.start, end=note.end)
    # Check for tags; check database for existing tags and generate new ones when needed
    if note.tags:
        # First get an array of the existing tags
        existing_tags = db.query(DbTag).filter(DbTag.tag.in_(note.tags)).all()
        print(existing_tags)
        Note.tags.extend(existing_tags)
        for each in note.tags:
            present = False

            for existing_tag in existing_tags:
                if present == False and existing_tag.tag == each:
                    #tag is already present
                    present = True

            if present == False:
                tag = db.merge(DbTag(tag=each))
                Note.tags.append(tag)
                print(tag)

    db.add(Note)
    db.commit()
    db.refresh(Note)
    return Note


@app.get("/api/v1/search/{key}")
def search_schools_and_contacts(key, db: Session = Depends(get_db)):
    return search.json_search(key, db)
