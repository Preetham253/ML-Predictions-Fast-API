#Dependency injection logic for API key and JWT token validation
from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_token

def get_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key

def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload

