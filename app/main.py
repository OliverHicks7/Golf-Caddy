from fastapi import FastAPI, HTTPException

from app import models
from app.agent import generate_recommendation
from app.database import SessionLocal, engine
from app.models import PlayerProfile
from app.schemas import (
    HoleInput,
    RecommendationResponse,
    PlayerProfileCreate,
    PlayerProfileUpdate,
    PlayerProfileResponse,
)


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Golf Caddie is up and running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/player-profile", response_model=PlayerProfileResponse)
def create_player_profile(profile: PlayerProfileCreate):
    db = SessionLocal()

    try:
        existing_profile = db.query(PlayerProfile).first()

        if existing_profile is not None:
            raise HTTPException(
                status_code=400,
                detail="A player profile already exists. Use PUT /player-profile to update it.",
            )

        new_profile = PlayerProfile(
            name=profile.name,
            handicap=profile.handicap,
            driver_distance=profile.driver_distance,
            seven_iron_distance=profile.seven_iron_distance,
            common_miss=profile.common_miss,
            current_focus=profile.current_focus,
        )

        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)

        return new_profile

    finally:
        db.close()

@app.get("/player-profile", response_model=PlayerProfileResponse)
def get_player_profile():
    db = SessionLocal()

    try:
        player_profile = db.query(PlayerProfile).first()

        if player_profile is None:
            raise HTTPException(
                status_code=404,
                detail="No player profile found. Use POST /player-profile to create one.",
            )

        return player_profile

    finally:
        db.close()

@app.put("/player-profile", response_model=PlayerProfileResponse)
def update_player_profile(profile: PlayerProfileUpdate):
    db = SessionLocal()

    try:
        player_profile = db.query(PlayerProfile).first()

        if player_profile is None:
            raise HTTPException(
                status_code=404,
                detail="No player profile found. Use POST /player-profile to create one.",
            )

        player_profile.name = profile.name
        player_profile.handicap = profile.handicap
        player_profile.driver_distance = profile.driver_distance
        player_profile.seven_iron_distance = profile.seven_iron_distance
        player_profile.common_miss = profile.common_miss
        player_profile.current_focus = profile.current_focus

        db.commit()
        db.refresh(player_profile)

        return player_profile

    finally:
        db.close()


@app.post("/recommendation", response_model=RecommendationResponse)
def create_recommendation(hole: HoleInput):
    return generate_recommendation(hole)