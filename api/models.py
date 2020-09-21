from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from .database import Base

class DbSchool(Base):
    __tablename__ = "schools"
    id = Column(Integer, Sequence('schools_id_seq'), index=True)
    school_id = Column(Integer, primary_key=True, index=True)
    lrkp_id = Column(String)
    school_type = Column(String, primary_key=True, index=True) # bso, opvang, po, vo
    brin = Column(String)
    vestigingsnummer = Column(String)
    naam = Column(String, primary_key=True, index=True)
    grondslag = Column(String)
    schoolwijzer_url = Column(String)
    onderwijsconcept = Column(String)
    heeft_voorschool = Column(Boolean, nullable=True, default=None)
    leerlingen = Column(Integer)
    address = Column(String) # adres/adres
    postcode = Column(String) # adres/postcode
    suburb = Column(String) # adres/stadsdeel
    website = Column(String) # adres/website
    email = Column(String) # adres/email
    phone = Column(String) # adres/telefoon
    city = Column(String) # adres/plaats
    point = Column(Geometry(geometry_type='POINT', srid=4326)) # coordinaten/lat & coordinaten/lon
