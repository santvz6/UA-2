from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from db import get_session, User

router = APIRouter(prefix= "/users")

@router.get("/")
def get_users(db : Session = Depends(get_session)):
    users = db.exec(select(User)).all()
    return users

@router.get("/{id}")
def get_user(user_id: int, db: Session = Depends(get_session)):
    user = db.get(id, User.id)