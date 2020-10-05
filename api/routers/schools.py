from fastapi import APIRouter, Depends, Request
from typing import List
from sqlalchemy.orm import Session
from api import school
from api.models.response import SchoolResponse

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/schools.geojson")
def get_all_schools_in_geojson_format(db: Session = Depends(get_db)):
    return school.geojson_all(db)


@router.get("/api/v1/schools")
def get_all_schools(db: Session = Depends(get_db)):
    return school.json_all(db)


@router.get("/api/v1/schools/{search}")
def search_for_schools(search, db: Session = Depends(get_db)):
    return school.json_search(search, db)
