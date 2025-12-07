from pydantic import BaseModel

class MovieData(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    