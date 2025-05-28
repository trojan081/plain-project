
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
import os
import sys
from middlewares.auth import AuthMiddleware
from middlewares.security_headers import SecurityHeadersMiddleware
from fastapi.staticfiles import StaticFiles


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

from routers import (
    demo, approval, auth, construction, invitation,
    organizations, project_status, projects, regulators,
    user_info, user_profile, llm_chat
)

for router in [
    auth, user_info, projects, approval, organizations,
    construction, regulators, project_status, invitation,
    user_profile, demo, llm_chat
]:
    app.include_router(router.router, prefix="/api")

app.add_middleware(AuthMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

static_path = "/app/frontend_dist"
if os.path.exists(static_path):
    app.mount("/", StaticFiles(directory=static_path, html=True), name="static")

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # замените на домен в проде
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return {"message": "pong"}

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    engine = create_engine(DATABASE_URL, echo=True)
else:
    print("⚠️ DATABASE_URL не задан — подключение к БД пропущено")

@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    index_path = os.path.join("/app/frontend_dist", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"detail": "Not Found"}