from typing import List, Optional
from pydantic import BaseModel, Field


class TagResponse(BaseModel):
    id: int
    tag: str
    notes: Optional[int] = 0

    class Config:
        orm_mode = True


class ContactResponse(BaseModel):
    id: int
    type: Optional[str] = "Contact"
    name: str = Field(alias='naam')
    email: Optional[str]
    phone: Optional[str]

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
    name: str = Field(alias='naam')
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
