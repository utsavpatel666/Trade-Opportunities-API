from fastapi import HTTPException, Header
import os

AUTH_TOKEN = os.getenv("AUTH_TOKEN")

def verify_token(token: str = Header(None)):
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return True
