import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from .config import SECRET_KEY, ALGORITHM


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):

        # Obtiene el token desde el encabezado Authorization
        token = request.headers.get("Authorization")
        
        if not token:
            raise HTTPException(
                status_code=401,
                detail="Authorization token is missing"
            )
        
        # El token llega en el formato "Bearer <token>", por lo que necesitamos separar el prefijo "Bearer"
        token = token.split(" ")[1]  # Eliminamos "Bearer " de la cabecera
        
        try:
            # Decodificamos el token usando la clave secreta y el algoritmo configurado
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            
            # Verificar si hay un 'sub' (el campo que almacena el nombre de usuario) en el payload
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(
                    status_code=401,
                    detail="Token is invalid"
                )
            
            return username
        
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Token has expired"
            )
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=401,
                detail="Token is invalid"
            )

# Validador de JWT que será utilizado en los endpoints
authenticator = JWTBearer()
