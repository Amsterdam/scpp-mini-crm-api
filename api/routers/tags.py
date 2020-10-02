from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api.models import Note, NoteCreate, DbNote, EnhancedNoteCreate, DbEnhancedNote, DbTag, DbSchool, DbContact
from api import tag

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/tags")
def get_all_tags(db: Session = Depends(get_db)):
    return tag.json_all(db)