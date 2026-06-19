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