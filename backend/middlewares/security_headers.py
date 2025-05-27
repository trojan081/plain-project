from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        headers = {
            "X-Content-Type-Options": "nosniff",
            # "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            # "X-XSS-Protection": "1; mode=block",
            # "X-Frame-Options": "DENY",
            # "Referrer-Policy": "no-referrer",
            # "Content-Security-Policy": "default-src 'self'",
            # "Expect-CT": "max-age=86400, enforce",
            # "Permissions-Policy": "geolocation=(), microphone=()",
            # "Cache-Control": "no-store",
            # "Content-Security-Policy": "default-src 'self'; img-src 'self' data:; font-src 'self'; script-src 'self'; style-src 'self'",
            # "Referrer-Policy": "strict-origin-when-cross-origin"

        }

        for k, v in headers.items():
            response.headers[k] = v

        return response
