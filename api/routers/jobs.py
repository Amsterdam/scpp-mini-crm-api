from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from api.database import engine, Base
from adapters.amsterdam import schools, tags

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/api/jobs")
def get_run_jobs(db: Session = Depends(get_db)):
    """
    Run the adapters to get data from remote sources.
    """
    try:
        Base.metadata.create_all(bind=engine)
        schools.run()
        tags.run()
    except:
        raise HTTPException(status_code=400, detail="Jobs failed, (or previously ran)")
    finally:
        db.close()
    return {"detail": "Jobs processed"}
