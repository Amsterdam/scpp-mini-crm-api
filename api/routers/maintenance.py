from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
import datetime
from api.database import engine, Base

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/status/database")
def get_status_database(db: Session = Depends(get_db)):
    try:
        Base.metadata.create_all(bind=engine)
    except:
        raise HTTPException(status_code=400, detail="No database connection")
    finally:
        db.close()
    return {"detail": "database connection OK"}


@router.get("/status/health")
def get_status_health():
    return {"detail": "api OK"}


@router.get("/status/time")
def get_status_health():
    current_datetime = datetime.datetime.now()
    return {"detail": {"time": current_datetime}}
