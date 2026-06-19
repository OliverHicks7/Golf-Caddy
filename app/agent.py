from app.schemas import HoleInput, RecommendationResponse
from app.tools import get_player_profile


def generate_recommendation(hole: HoleInput) -> RecommendationResponse:
    """
    Generate a basic golf strategy recommendation.

    This version uses a simple player profile tool.
    Later, this function will call more tools such as weather,
    course data, shot history, and an AI model.
    """

    player_profile = get_player_profile()

    recommendation = "Play a conservative tee shot."
    reasoning_parts = []
    confidence = "medium"

    common_miss = player_profile["common_miss"]
    driver_distance = player_profile["driver_distance"]
    current_focus = player_profile["current_focus"]

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