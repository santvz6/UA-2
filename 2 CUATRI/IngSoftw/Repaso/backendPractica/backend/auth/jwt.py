from fastapi import Request
from fastapi.security import HTTPBearer

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        return ""

authenticator = JWTBearer()
