from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class ContactBase(BaseModel):
    name: str


class ContactCreate(ContactBase):
    phone: str
    email: Optional[str]
    school_id: Optional[int]


class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True


class NoteCreate(BaseModel):
    note: str
    contact_id: int


class Note(NoteCreate):
    id: int

    class Config:
        orm_mode = True


class TagCreate(BaseModel):
    tag: str


class Tag(TagCreate):
    id: int

    class Config:
        orm_mode = True


class EnhancedNoteBase(BaseModel):
    note: str
    tags: Optional[List[str]]
    contacts: Optional[List[int]]
    schools: Optional[List[int]]


class EnhancedNoteCreate(EnhancedNoteBase):
    start: Optional[datetime]
    end: Optional[datetime]


class EnhancedNote(EnhancedNoteCreate):
    id: int

    class Config:
        orm_mode = True
