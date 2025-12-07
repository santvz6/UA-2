from pydantic import BaseModel

# Modelo para crear un comentario (input)
class CommentCreate(BaseModel):
    user_id: int 
    text: str  

# Modelo para crear una película (input)
class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    genre: str  

# Modelo para almacenar el JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Modelo para hacer Login
class LoginRequest(BaseModel):
    username: str
    password: str

class SentimentRequest(BaseModel):
    text: str