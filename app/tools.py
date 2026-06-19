from app.database import SessionLocal
from app.models import PlayerProfile


def get_player_profile():
    """
    Return the player's profile from the database.

    This tool should only read existing memory.
    It should not create a default profile automatically.
    """

    db = SessionLocal()

    try:
        player_profile = db.query(PlayerProfile).first()

        if player_profile is None:
            return None

        return {
            "name": player_profile.name,
            "handicap": player_profile.handicap,
            "driver_distance": player_profile.driver_distance,
            "seven_iron_distance": player_profile.seven_iron_distance,
            "common_miss": player_profile.common_miss,
            "current_focus": player_profile.current_focus,
        }

    finally:
        db.close()


def get_weather_conditions(course_name: str | None = None):
    """
    Return basic weather conditions.

    For now this is hardcoded.
    Later this can call a real weather API using the course location.
    """

    return {
        "course_name": course_name,
        "wind_speed_mph": 15,
        "wind_direction": "left_to_right",
        "conditions": "dry",
    }