from fastapi import Depends, FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from .routers import notes, schools, contacts, search, tags, maintenance
from .database import SessionLocal, engine
from .settings import settings

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers moved to individual files in the ./routers folder
app.include_router(notes.router)
app.include_router(schools.router)
app.include_router(contacts.router)
app.include_router(search.router)
app.include_router(tags.router)
app.include_router(maintenance.router)
