def get_player_profile():
    """
    Return a basic player profile.

    For now this is hardcoded.
    Later this can come from a database.
    """

    return {
        "handicap": 54,
        "driver_distance": 180,
        "seven_iron_distance": 120,
        "common_miss": "left",
        "current_focus": "controlled tempo and keeping the ball in play",
    }

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