from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from db import get_session
from db import User, Comment, Movie

router = APIRouter(prefix="/users", tags=["Users"])

######################
### GET
@router.get("/")
def get_users(db: Session = Depends(get_session)):
    """ 
    Obtiene todos los usuarios almacenados en la base de datos.
    Devuelve una lista de usuarios con solo los campos 'id' y 'username'.
    """
    users = db.exec(select(User)).all()
    return [user.model_dump(include={"id", "username"}) for user in users]


@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_session)):
    """ 
    Obtiene un usuario por su ID.
    Si el usuario no existe, devuelve un error 404.
    Devuelve los detalles del usuario, incluidos 'id', 'username', y 'email'.
    """
    user = db.exec(select(User).where(User.id == id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.model_dump(include={"id", "username", "email"})

@router.get("/{user_id}/comments")
def get_comments_by_user(user_id: int, db: Session = Depends(get_session)):
    """ 
    Obtiene todos los comentarios hechos por un usuario, especificado por su ID.
    Si el usuario no existe, devuelve un error 404.
    Para cada comentario, obtiene los detalles de la película asociada.
    """
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    comments = db.exec(select(Comment).where(Comment.user_id == user_id)).all()
    result = []

    # Es muy importante eliminar los comentarios que el usuario tenía
    # para no dejar referencias en un null object
    for comment in comments:
        movie = db.get(Movie, comment.movie_id)
        result.append({
            "movie_id": comment.movie_id,
            "title": movie.title if movie else None,
            "user_id": comment.user_id,
            "username": user.username,
            "text": comment.text,
            "sentiment": comment.sentiment
        })
    return result
