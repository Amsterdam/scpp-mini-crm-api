from . import school, contact, note
from fastapi import FastAPI
from .settings import settings
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/schools.geojson")
def get_schools_geojson():
    return school.geojson_all()

@app.get("/api/v1/schools")
def get_schools_json():
    return school.json_all()


@app.get("/api/v1/schools/{search}")
def get_schools_search_json(search):
    return school.json_search(search)

@app.get("/api/v1/contacts")
def get_contacts():
    return contact.json_all()


@app.get("/api/v1/contacts/{id}")
def get_contact(id):
    return


@app.post("/api/v1/contacts")
def post_contact():
    return


@app.delete("/api/v1/contacts")
def delete_contact():
    return


@app.get("/api/v1/notes")
def get_notes():
    return note.json_all()


@app.get("/api/v1/notes/{id}")
def get_note(id):
    return


@app.get("/api/v1/notes/{year}/{month}/{day}")
def get_notes(year, month, day):
    return


@app.post("/api/v1/notes")
def post_note():
    return


@app.delete("/api/v1/notes")
def delete_note():
    return