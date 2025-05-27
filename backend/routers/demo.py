from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os, shutil, subprocess, traceback


router = APIRouter(prefix="/demo")

UPLOAD_DIR = '/tmp/demo_uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_PATH = os.path.join(BASE_DIR, 'scripts', 'demo_process.py')

@router.post("/upload")
async def upload_demo_file(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.dxf'):
        raise HTTPException(status_code=400, detail='Требуется файл в формате .dxf')

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    dxf_path = filepath  # тк .dxf

    try:
        with open(filepath, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Запуск demo_process.py
        try:
            result = subprocess.run(
                ["python3", SCRIPT_PATH, dxf_path],
                capture_output=True, text=True, timeout=60
            )
            output = result.stdout + '\n' + result.stderr
        except Exception as e:
            output = traceback.format_exc()

        return JSONResponse(content={'result': output})

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
