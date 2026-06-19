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

class PlayerProfileResponse(BaseModel):
    id: int
    name: str
    handicap: int
    driver_distance: int
    seven_iron_distance: int
    common_miss: str
    current_focus: str


class PlayerProfileUpdate(BaseModel):
    name: str
    handicap: int
    driver_distance: int
    seven_iron_distance: int
    common_miss: str
    current_focus: str