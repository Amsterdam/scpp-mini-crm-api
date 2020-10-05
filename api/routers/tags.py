from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api.models.response import TagResponse

from api import tag

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/v1/tags", response_model=List[TagResponse], response_model_exclude_none=True)
def get_all_tags(db: Session = Depends(get_db)):
    return tag.json_all(db)