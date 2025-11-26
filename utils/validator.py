from fastapi import HTTPException
import re

def validate_sector_name(sector: str):
    if not re.match(r"^[A-Za-z\s]+$", sector):
        raise HTTPException(status_code=400, detail="Invalid sector name")
    return True
