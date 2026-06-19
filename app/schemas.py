from pydantic import BaseModel


class HoleInput(BaseModel):
    course_name: str | None = None
    hole_number: int | None = None
    tee_name: str | None = None

    yardage: int
    par: int
    stroke_index: int | None = None

    fairway_width: str | None = None
    hazards: str | None = None
    notes: str | None = None


class RecommendationResponse(BaseModel):
    recommendation: str
    reasoning: str
    confidence: str