from fastapi import FastAPI
from pydantic import BaseModel

from app.model.model import __version__ as model_version
from app.model.model import predict_pipeline

app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
async def predict(text_in: TextIn):
    language = predict_pipeline(text_in.text)
    return {"language": language}
