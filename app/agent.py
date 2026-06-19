from app.schemas import HoleInput, RecommendationResponse
from app.tools import get_player_profile, get_weather_conditions


def generate_recommendation(hole: HoleInput) -> RecommendationResponse:
    """
    Generate a basic golf strategy recommendation.

    This version uses two tools:
    - player profile
    - weather conditions

    Later, this function will call real APIs, player memory, and an AI model.
    """

    player_profile = get_player_profile()
    if player_profile is None:
        return RecommendationResponse(
            recommendation="Create a player profile before requesting a recommendation.",
            reasoning="The caddie needs your handicap, distances, common miss, and current focus before it can give useful personalised advice.",
            confidence="low",
        )

    weather = get_weather_conditions(hole.course_name)

    recommendation = "Play a conservative tee shot."
    reasoning_parts = []
    confidence = "medium"

    common_miss = player_profile["common_miss"]
    driver_distance = player_profile["driver_distance"]
    current_focus = player_profile["current_focus"]

    wind_speed = weather["wind_speed_mph"]
    wind_direction = weather["wind_direction"]
    conditions = weather["conditions"]

    if hole.par == 3:
        recommendation = "Choose the club that gives you a comfortable full swing to the centre of the green."
        reasoning_parts.append(
            "On a par 3, the priority is hitting the green or leaving a simple miss."
        )

    elif hole.par == 4:
        if hole.yardage >= 400:
            recommendation = "Consider driver only if there is enough room for your usual miss."
            reasoning_parts.append(
                f"This is a longer par 4. Your driver distance is around {driver_distance} yards, so driver may help, but only if the miss pattern is manageable."
            )
        else:
            recommendation = "Consider a controlled tee shot with a fairway wood, hybrid, or long iron."
            reasoning_parts.append(
                "This par 4 is not especially long, so position may be more valuable than maximum distance."
            )

    elif hole.par == 5:
        recommendation = "Focus on keeping the tee shot in play and setting up a sensible second shot."
        reasoning_parts.append(
            "On a par 5, avoiding penalties is usually more important than trying to force a heroic shot."
        )

    if hole.fairway_width and hole.fairway_width.lower() == "narrow":
        recommendation = "Take less than driver and aim for the safest part of the fairway."
        reasoning_parts.append(
            "The fairway is narrow, so accuracy is more valuable than distance."
        )

    if common_miss == "left":
        reasoning_parts.append(
            "Your current common miss is left, so avoid aiming too close to trouble on the left side."
        )

    if wind_speed >= 15:
        reasoning_parts.append(
            f"The wind is significant at around {wind_speed} mph, so club selection and shot shape need extra caution."
        )

    if wind_direction == "left_to_right":
        reasoning_parts.append(
            "The wind is moving left to right, which may exaggerate shots that start or curve that way."
        )

    if conditions == "dry":
        reasoning_parts.append(
            "Dry conditions may allow more rollout, so a shorter club from the tee may still leave a manageable approach."
        )

    if hole.hazards:
        reasoning_parts.append(f"Important hazards to consider: {hole.hazards}.")

    if hole.stroke_index is not None and hole.stroke_index <= 6:
        reasoning_parts.append(
            "This is one of the harder holes on the course, so a bogey-friendly strategy is sensible."
        )

    if hole.notes:
        reasoning_parts.append(f"Additional notes: {hole.notes}.")

    reasoning_parts.append(f"Your current improvement focus is: {current_focus}.")

    reasoning = " ".join(reasoning_parts)

    if not reasoning:
        reasoning = "There is limited hole context, so the safest recommendation is to prioritise keeping the ball in play."
        confidence = "low"

    return RecommendationResponse(
        recommendation=recommendation,
        reasoning=reasoning,
        confidence=confidence,
    )