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


@router.get("/api/v2/school/{id}", response_model=SchoolResponse, response_model_exclude_none=True, response_model_by_alias=False)
def get_school_by_id(id, db: Session = Depends(get_db)):
    return school.by_id(id, db)
