from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from db import get_session, Movie
from .models import MovieData


router = APIRouter(prefix="/movies")

@router.get("/")
def get_movies(db: Session = Depends(get_session)):
    movies = db.exec(select(Movie)).all()
    return movies

@router.get("/{id}")
def get_movie(movie_id: int, db:Session = Depends(get_session)):
    movie = db.get(movie_id, Movie)
    return movie

@router.post("/")
def post_movie(movieData: MovieData, db: Session = Depends(get_session)):
    movie = Movie(
        title= movieData.title,
        director= movieData.director,
        year= movieData.year,
        genre= movieData.genre 
        )
    db.add(movie)
    db.commit()
    db.refresh()
    return movie

@router.delete("/{id}")
def delete_movie(movie_id: int, db: Session = Depends(get_session)):
    movie = db.get(movie_id, Movie)
    db.delete(movie)
    db.commit()
    return {"message": "Película eliminada."}
