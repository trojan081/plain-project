from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from fastapi import Request
from utils.auth import SECRET_KEY, ALGORITHM

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.cookies.get("access_token")
        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                request.state.user_id = payload.get("sub")
            except JWTError:
                request.state.user_id = None
        else:
            request.state.user_id = None

        return await call_next(request)
