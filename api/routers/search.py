from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api import search
from ..dependencies import get_user

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/search/{key}")
def search_schools_and_contacts(key, db: Session = Depends(get_db), user: str = Depends(get_user)):
    return search.json_search(key, db)