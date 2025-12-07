from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    username: str = Field(max_length=100, unique=True)
    email: str = Field(max_length=255, unique=True)
    password: str = Field(max_length=255)

    comments: list["Comment"] = Relationship(back_populates="user")  # Cada usuario tiene muchos comentarios

class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str = Field(max_length=255)
    director: str = Field(max_length=100)
    year: int  
    genre: str = Field(max_length=100) 
    comments: list["Comment"] = Relationship(back_populates="movie") # Cada película tiene muchos comentarios

class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    text: str = Field(max_length=255)
    sentiment: str
    
    movie_id: int = Field(foreign_key="movie.id")
    movie: Movie | None = Relationship(back_populates="comments") # Cada comentario pertenece a una película

    user_id: int = Field(foreign_key="user.id")
    user: User | None = Relationship(back_populates="comments") # Cada comentario pertenece a un usuario

