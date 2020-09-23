from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from .database import Base

class ContactBase(BaseModel):
    name: str


class ContactCreate(ContactBase):
    phone: str
    email: str
    school_id: int


class Contact(ContactBase):
    id: int

    class Config: 
        orm_mode = True


class DbContact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, index=True, primary_key=True)
    naam = Column(String, unique=True, index=True)
    email = Column(String)
    phone = Column(String)
    school_id = Column(Integer, ForeignKey('schools.id'))
    school = relationship("DbSchool", back_populates="contacts")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    notes = relationship("DbNote")


class NoteCreate(BaseModel):
    note: str
    contact_id: int


class Note(NoteCreate):
    id: int

    class Config: 
        orm_mode = True


class DbNote(Base):
    __tablename__ = "notes"
    id = Column(Integer, index=True, primary_key=True)
    note = Column(String)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("DbContact", back_populates="notes")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class DbSchool(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, primary_key=True)
    lrkp_id = Column(String)
    school_type = Column(String, primary_key=True)  # bso, opvang, po, vo
    brin = Column(String)
    vestigingsnummer = Column(String)
    naam = Column(String, primary_key=True, index=True)
    grondslag = Column(String)
    schoolwijzer_url = Column(String)
    onderwijsconcept = Column(String)
    heeft_voorschool = Column(Boolean, nullable=True, default=None)
    leerlingen = Column(Integer)
    address = Column(String)  # adres/adres
    postcode = Column(String)  # adres/postcode
    suburb = Column(String)  # adres/stadsdeel
    website = Column(String)  # adres/website
    email = Column(String)  # adres/email
    phone = Column(String)  # adres/telefoon
    city = Column(String)  # adres/plaats
    point = Column(Geometry(geometry_type='POINT', srid=4326))  # coordinaten/lat & coordinaten/lon
    contacts = relationship("DbContact")
