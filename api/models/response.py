from typing import List, Optional
from datetime import datetime
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
    name: str = Field(...,alias='naam')
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
    name: str = Field(...,alias='naam')
    address: str

    class Config:
        orm_mode = True


class NoteResponse(BaseModel):
    contact: ContactResponse
    note: str
    tags: Optional[List[TagResponse]] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    contacts: Optional[List[ContactResponse]] = None
    schools: Optional[List[SchoolResponse]] = None

    class Config:
        orm_mode = True
