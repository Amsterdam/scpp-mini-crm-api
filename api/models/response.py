from typing import List, Optional
from pydantic import BaseModel, Field


class TagResponse(BaseModel):
    id: int
    tag: str
    type: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[int] = None

    class Config:
        orm_mode = True


class ContactResponse(BaseModel):
    id: int
    type: Optional[str] = "Contact"
    name: str = Field('naam')
    email: Optional[str] = None
    phone: Optional[str] = None

    # school_id: Optional[int]

    class Config:
        orm_mode = True


class SchoolResponse(BaseModel):
    type: Optional[str] = "School"
    id: int
    school_id: Optional[int]
    lrkp_id: Optional[int]
    school_type: str
    brin: Optional[str]
    vestigingsnummer: Optional[str]
    name: str = Field('naam')
    address: str

    class Config:
        orm_mode = True


class NoteResponse(BaseModel):
    note: Optional[str]
    tags: Optional[List[TagResponse]] = []
    contacts: Optional[List[ContactResponse]] = []
    schools: Optional[List[SchoolResponse]] = []

    class Config:
        orm_mode = True
