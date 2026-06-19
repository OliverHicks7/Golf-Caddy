from app.database import SessionLocal
from app.models import PlayerProfile


def get_player_profile():
    """
    Return the player's profile from the database.

    If no profile exists yet, create a default one.
    Later, we can add endpoints to update this properly.
    """

    db = SessionLocal()

    try:
        player_profile = db.query(PlayerProfile).first()

        if player_profile is None:
            player_profile = PlayerProfile(
                name="Oliver Hicks",
                handicap=20,
                driver_distance=200,
                seven_iron_distance=125,
                common_miss="left",
                current_focus="controlled tempo and keeping the ball in play",
            )

            db.add(player_profile)
            db.commit()
            db.refresh(player_profile)

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