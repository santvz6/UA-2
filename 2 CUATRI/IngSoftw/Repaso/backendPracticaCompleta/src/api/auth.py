from fastapi import APIRouter, Depends
from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from auth import create_access_token, verify_password, authenticator
from db import get_session, User
from .pydantic_models import Token, LoginRequest


router = APIRouter()

# Ejemplo de uso (utilizando Postman) -> http://localhost:8000/protected
# Authorization:
# -> Bearer Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBbGljZSIsImV4cCI6MTc0MzYxOTU2N30.wuzcdGivc1I2wKOckjNXiWV036_AxM72QFL57GcqmEQ
# Return:
#{
#    "message": "This is a protected route"
#}
@router.get("/protected", dependencies=[Depends(authenticator)])
async def protected_route():
    return {"message": "This is a protected route"}

# Ejemplo de uso (utilizando Postman) -> http://localhost:8000/login/
# Body:
#{
#    "username": "Alice",
#    "password": "password123"
#}
# Return (información privada):
#{
#    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBbGljZSIsImV4cCI6MTc0MzYxOTU2N30.wuzcdGivc1I2wKOckjNXiWV036_AxM72QFL57GcqmEQ",
#    "token_type": "bearer"
#}

@router.post("/login", response_model=Token)
async def login_for_access_token(login_data: LoginRequest, db: Session = Depends(get_session)):
    
    user = db.exec(select(User).where(User.username == login_data.username)).first()
    
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")