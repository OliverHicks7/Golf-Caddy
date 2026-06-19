from fastapi import FastAPI

from app import models
from app.agent import generate_recommendation
from app.database import engine
from app.schemas import HoleInput, RecommendationResponse


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Golf Caddie is up and running"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/recommendation", response_model=RecommendationResponse)
def create_recommendation(hole: HoleInput):
    return generate_recommendation(hole)