from .settings import settings
import json
import urllib.request
from api.database import SessionLocal, engine
from api.models.tables import DbSchool
from geoalchemy2 import functions

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def run_po():
    """
    Adapter to grab schools from the API of the City of Amsterdam
    See https://schoolwijzer.amsterdam.nl/nl/api/documentatie
    """
    connect_string = settings.AMSTERDAM_PRIMARY_SCHOOLS
    url = urllib.request.urlopen(connect_string)
    if url.getcode() == 200:
        data = url.read()
        # Start inserting
        result = json.loads(data)
        db = SessionLocal()

        try:
            DbSchool.__table__.create(engine)
        except:
            pass

        for entry in result["results"]:
            row = DbSchool(
                school_id = entry["id"],
                brin = entry["brin"],
                vestigingsnummer = entry["vestigingsnummer"],
                school_type = "po",
                naam = entry["naam"],
                grondslag = entry["grondslag"],
                schoolwijzer_url = entry["schoolwijzer_url"],
                address = entry["adres"]["adres"],
                suburb = entry["adres"]["stadsdeel"],
                postcode = entry["adres"]["postcode"],
                website = entry["adres"]["website"],
                email = entry["adres"]["email"],
                phone = entry["adres"]["telefoon"],
                city = entry["adres"]["plaats"],
                onderwijsconcept = entry["onderwijsconcept"],
                heeft_voorschool = entry["heeft_voorschool"],
                leerlingen = entry["leerlingen"],
                point=functions.ST_GeomFromText("POINT(" + str(entry["coordinaten"]["lng"]) + " " + str(entry["coordinaten"]["lat"]) + ")", 4326)
            )
            db.merge(row)
        db.commit()


def run_vo():
    """
    Adapter to grab schools from the API of the City of Amsterdam
    See https://schoolwijzer.amsterdam.nl/nl/api/documentatie
    """
    connect_string = settings.AMSTERDAM_HIGH_SCHOOLS
    url = urllib.request.urlopen(connect_string)
    if url.getcode() == 200:
        data = url.read()
        # Start inserting
        result = json.loads(data)
        db = SessionLocal()

        try:
            DbSchool.__table__.create(engine)
        except:
            pass

        for entry in result["results"]:
            row = DbSchool(
                school_id = entry["id"],
                brin = entry["brin"],
                vestigingsnummer = entry["vestigingsnummer"],
                school_type = "vo",
                naam = entry["naam"],
                grondslag = entry["grondslag"],
                schoolwijzer_url = entry["schoolwijzer_url"],
                address = entry["adres"]["adres"],
                suburb = entry["adres"]["stadsdeel"],
                postcode = entry["adres"]["postcode"],
                website = entry["adres"]["website"],
                email = entry["adres"]["email"],
                phone = entry["adres"]["telefoon"],
                city = entry["adres"]["plaats"],
                onderwijsconcept = entry["onderwijsconcept"],
                leerlingen = entry["leerlingen"],
                point=functions.ST_GeomFromText("POINT(" + str(entry["coordinaten"]["lng"]) + " " + str(entry["coordinaten"]["lat"]) + ")", 4326)
            )
            db.merge(row)
        db.commit()


def run_bso():
    """
    Adapter to grab schools from the API of the City of Amsterdam
    See https://schoolwijzer.amsterdam.nl/nl/api/documentatie
    """
    connect_string = settings.AMSTERDAM_KINDERGARTEN
    url = urllib.request.urlopen(connect_string)
    if url.getcode() == 200:
        data = url.read()
        # Start inserting
        result = json.loads(data)
        db = SessionLocal()

        try:
            DbSchool.__table__.create(engine)
        except:
            pass

        for entry in result["results"]:
            row = DbSchool(
                school_id = entry["id"],
                lrkp_id = entry["lrkp_id"],
                school_type = "opvang",
                naam = entry["naam"],
                schoolwijzer_url = entry["schoolwijzer_url"],
                address = entry["adres"]["adres"],
                postcode = entry["adres"]["postcode"],
                suburb = entry["adres"]["stadsdeel"],
                website = entry["adres"]["website"],
                email = entry["adres"]["email"],
                phone = entry["adres"]["telefoon"],
                city = entry["adres"]["plaats"],
                point=functions.ST_GeomFromText("POINT(" + str(entry["coordinaten"]["lng"]) + " " + str(entry["coordinaten"]["lat"]) + ")", 4326)
            )
            db.merge(row)
        db.commit()

def run_opvang():
    """
    Adapter to grab schools from the API of the City of Amsterdam
    See https://schoolwijzer.amsterdam.nl/nl/api/documentatie
    """
    connect_string = settings.AMSTERDAM_DAYCARE
    url = urllib.request.urlopen(connect_string)
    if url.getcode() == 200:
        data = url.read()
        # Start inserting
        result = json.loads(data)
        db = SessionLocal()

        try:
            DbSchool.__table__.create(engine)
        except:
            pass

        for entry in result["results"]:
            row = DbSchool(
                school_id = entry["id"],
                lrkp_id = entry["lrkp_id"],
                school_type = "bso",
                naam = entry["naam"],
                schoolwijzer_url = entry["schoolwijzer_url"],
                address = entry["adres"]["adres"],
                suburb = entry["adres"]["stadsdeel"],
                postcode = entry["adres"]["postcode"],
                website = entry["adres"]["website"],
                email = entry["adres"]["email"],
                phone = entry["adres"]["telefoon"],
                city = entry["adres"]["plaats"],
                point=functions.ST_GeomFromText("POINT(" + str(entry["coordinaten"]["lng"]) + " " + str(entry["coordinaten"]["lat"]) + ")", 4326)
            )
            db.merge(row)
        db.commit()


def run():
    run_po()
    run_vo()
    run_opvang()
    run_bso()
