import bcrypt
from datetime import datetime, timedelta, timezone
from jwt import encode
from .config import SECRET_KEY, ALGORITHM


def verify_password(plain_password, hashed_password):
    """ Verifica si la contraseña en texto plano coincide con la contraseña encriptada"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """ Crea un token de acceso JWT con una fecha de expiración"""
    to_encode = data.copy()
    
    expire = datetime.now(tz=timezone.utc) + expires_delta if expires_delta else datetime.now(tz=timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  
    return encoded_jwt
