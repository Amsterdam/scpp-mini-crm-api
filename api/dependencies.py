from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from .settings import settings

security = HTTPBasic()

def get_user(credentials: HTTPBasicCredentials = Depends(security)):
    valid = False
    if credentials.username in settings.USERS.keys():
        if secrets.compare_digest(credentials.password, settings.USERS[credentials.username]):
            valid = True
    if valid == False:
        raise HTTPException(status_code=401, detail="Please login", headers={"WWW-Authenticate": "Basic"})
    return credentials.username
