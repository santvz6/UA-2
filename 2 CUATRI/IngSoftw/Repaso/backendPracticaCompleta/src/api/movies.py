from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from db import get_session
from db import Movie, User, Comment
from ia import SentimentModel
from .pydantic_models import MovieCreate, CommentCreate

router = APIRouter(prefix="/movies", tags=["Movies"])

######################
### GET
@router.get("/")
def get_movies(db: Session = Depends(get_session)):
    """ 
    Obtiene todas las películas almacenadas en la base de datos.
    Devuelve una lista de todas las películas.
    """
    movies = db.exec(select(Movie)).all() 
    return movies

@router.get("/search")
def search_movies(title: str, db: Session = Depends(get_session)):
    """ 
    Realiza una búsqueda de películas por título.
    Devuelve una lista de películas cuyo título coincida parcialmente con el texto proporcionado.
    """
    movies = db.exec(select(Movie).where(Movie.title.ilike(f"%{title}%"))).all()
    return movies

@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_session)):
    """ 
    Obtiene los detalles de una película por su ID.
    Si la película no existe, devuelve un error 404.
    """
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.get("/{movie_id}/comments")
def get_comments_by_movie(movie_id: int, db: Session = Depends(get_session)):
    """ 
    Obtiene los comentarios asociados a una película por su ID.
    Si la película no existe, devuelve un error 404.
    """
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    comments = db.exec(select(Comment).where(Comment.movie_id == movie_id)).all()
    
    result = []
    for comment in comments:
        user = db.get(User, comment.user_id)
        result.append({
            "movie_id": comment.movie_id,
            "title": movie.title,
            "user_id": comment.user_id,
            "username": user.username if user else None,
            "text": comment.text,
            "sentiment": comment.sentiment
        })
    
    return result

######################
### POST
@router.post("/", status_code=201)
def create_movie(movie_data: MovieCreate, db: Session = Depends(get_session)):
    """ 
    Crea una nueva película en la base de datos.
    Recibe los datos de la película en formato MovieCreate.
    """
    movie = Movie(**movie_data.dict())  # Convertimos MovieCreate a dict
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

@router.post("/{movie_id}/comments", status_code=201)
def add_comment(movie_id: int, comment_data: CommentCreate, db: Session = Depends(get_session)):
    """ 
    Añade un comentario a una película especificada por su ID.
    Realiza un análisis de sentimiento del comentario antes de guardarlo.
    Si la película o el usuario no existen, devuelve un error 404.
    """
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    user = db.get(User, comment_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    sentiment = SentimentModel.analyze_sentiment(comment_data.text)
    
    if sentiment is None:
        raise HTTPException(status_code=400, detail="Sentiment analysis failed")

    new_comment = Comment(
        text=comment_data.text,
        sentiment=sentiment,
        movie_id=movie_id,
        user_id=comment_data.user_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return {
        "movie_id": new_comment.movie_id,
        "title": movie.title,
        "user_id": new_comment.user_id,
        "username": user.username,
        "text": new_comment.text,
        "sentiment": new_comment.sentiment
    }

######################
### DELETE
@router.delete("/{id}", status_code=200)
def delete_movie(id: int, db: Session = Depends(get_session)):
    """ 
    Elimina una película y sus comentarios asociados por su ID.
    Si la película no existe, devuelve un error 404.
    """
    movie = db.get(Movie, id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Es muy importante eliminar los comentarios que la película tenía
    # para no dejar referencias en un null object
    comments = db.exec(select(Comment).where(Comment.movie_id == id)).all()
    for comment in comments:
        db.delete(comment)
    
    db.delete(movie)
    db.commit()

    return {"message": "Movie and its comments deleted successfully"}
