from sqlmodel import SQLModel, create_engine, Session
from db.models import User
import bcrypt

# Configurar la conexión a MySQL
DATABASE_URL = "mysql+pymysql://user:password@localhost/movies"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Función para obtener la sesión de base de datos
def get_session():
    session = Session(engine)
    try:
        return session  # Devolvemos la sesión directamente
    except Exception as e:
        session.rollback()  # Hacemos rollback si hay un error
        raise e
    finally:
        session.close()  # Nos aseguramos de cerrar la sesión cuando se salga de la función

# Función para crear las tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Función para eliminar las tablas de la base de datos
def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8') 

def seed_users():
    with get_session() as session:
        users = [
            User(username="Alice", email="alice@example.com", password=hash_password("password123")),
            User(username="Bob", email="bob@example.com", password=hash_password("password456")),
            User(username="Charlie", email="charlie@example.com", password=hash_password("password789")),
        ]
        session.add_all(users)        
        session.commit()
