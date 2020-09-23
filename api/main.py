from fastapi import Depends, FastAPI, Request, Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from . import school, contact, note
from .database import SessionLocal, engine, Base
from .settings import settings
from .models import Contact, ContactCreate, DbContact

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


@app.get("/api/v1/contacts/{id}")
def get_contact(id, db: Session = Depends(get_db)):
    return


@app.post("/api/v1/contacts")
async def post_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if contact.school_id > 0:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone, school_id=contact.school_id)
    else:
        Contact = DbContact(naam=contact.name, email=contact.email, phone=contact.phone)

    db.add(Contact)
    db.commit()
    db.refresh(Contact)
    print(Contact)
    return Contact


@app.delete("/api/v1/contacts")
def delete_contact(db: Session = Depends(get_db)):
    return


@app.get("/api/v1/notes")
def get_notes(db: Session = Depends(get_db)):
    return note.json_all(db)


@app.get("/api/v1/notes/{id}")
def get_note(id, db: Session = Depends(get_db)):
    return


@app.get("/api/v1/notes/{year}/{month}/{day}")
def get_notes(year, month, day, db: Session = Depends(get_db)):
    return


@app.post("/api/v1/notes")
def post_note(db: Session = Depends(get_db)):
    return


@app.delete("/api/v1/notes")
def delete_note(db: Session = Depends(get_db)):
    return
