from fastapi import FastAPI, UploadFile, File
import shutil
import os
from model_utils import predict_arrhythmia

app = FastAPI(title="Arrhythmia Detection API")

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = predict_arrhythmia(file_path)
    finally:
        os.remove(file_path)

    return result