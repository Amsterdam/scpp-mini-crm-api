from fastapi import APIRouter, Depends, Request
from typing import List
from sqlalchemy.orm import Session
from api.models.create import Note, NoteCreate, EnhancedNote, EnhancedNoteCreate
from api.models.response import NoteResponse
from api.models.tables import DbEnhancedNote, DbNote, DbTag, DbSchool, DbContact
from api import note, enhanced_note

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/notes", deprecated=True)
def get_all_notes(db: Session = Depends(get_db)):
    return note.json_all(db)


@router.get("/api/v1/notes/{contact_id}", deprecated=True)
def get_notes_by_contact_id(contact_id, db: Session = Depends(get_db)):
    return note.json_by_contact_id(contact_id, db)


@router.post("/api/v1/note", deprecated=True)
async def post_note(note: NoteCreate, db: Session = Depends(get_db)):
    Note = DbNote(note=note.note, contact_id=note.contact_id)
    db.add(Note)
    db.commit()
    db.refresh(Note)
    return Note


@router.get("/api/v2/notes", response_model=List[NoteResponse])
def get_all_enhanced_notes(db: Session = Depends(get_db)):
    return enhanced_note.json_all(db)


@router.post("/api/v2/note")
async def post_enhanced_note(note: EnhancedNoteCreate, db: Session = Depends(get_db)):
    Note = DbEnhancedNote(note=note.note, start=note.start, end=note.end, contact_id=note.contact_id)
    # Check for tags; check database for existing tags and generate new ones when needed
    if note.tags:
        # First get an array of the existing tags
        existing_tags = db.query(DbTag).filter(DbTag.tag.in_(note.tags)).all()
        Note.tags.extend(existing_tags)
        for each in note.tags:
            present = False

            for existing_tag in existing_tags:
                if present == False and existing_tag.tag == each:
                    # tag is already present
                    present = True

            if present == False:
                tag = db.merge(DbTag(tag=each))
                Note.tags.append(tag)
        # Check for tags; check database for existing tags and generate new ones when needed
    if note.schools:
        # First get an array of the existing tags
        schools = db.query(DbSchool).filter(DbSchool.id.in_(note.schools)).all()
        Note.schools.extend(schools)
    
    if note.contacts:
        # First get an array of the existing tags
        contacts = db.query(DbContact).filter(DbContact.id.in_(note.contacts)).all()
        Note.contacts.extend(contacts)

    db.add(Note)
    db.commit()
    db.refresh(Note)
    return Note
