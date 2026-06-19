from app.schemas import HoleInput, RecommendationResponse


def generate_recommendation(hole: HoleInput) -> RecommendationResponse:
    """
    Generate a basic golf strategy recommendation.

    This is a simple rule-based version for the MVP.
    Later, this function will become the place where we call tools,
    player memory, weather APIs, and eventually an LLM.
    """

    recommendation = "Play a conservative tee shot."
    reasoning_parts = []
    confidence = "medium"

    if hole.par == 3:
        recommendation = "Choose the club that gives you a comfortable full swing to the centre of the green."
        reasoning_parts.append(
            "On a par 3, the priority is hitting the green or leaving a simple miss."
        )

    elif hole.par == 4:
        if hole.yardage >= 400:
            recommendation = "Consider driver if the fairway is forgiving, but avoid forcing extra distance."
            reasoning_parts.append(
                "This is a longer par 4, so distance matters, but keeping the ball in play is still the priority."
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

    if hole.hazards:
        reasoning_parts.append(f"Important hazards to consider: {hole.hazards}.")

    if hole.stroke_index is not None and hole.stroke_index <= 6:
        reasoning_parts.append(
            "This is one of the harder holes on the course, so a bogey-friendly strategy is sensible."
        )

    if hole.notes:
        reasoning_parts.append(f"Additional notes: {hole.notes}.")

    reasoning = " ".join(reasoning_parts)

    if not reasoning:
        reasoning = "There is limited hole context, so the safest recommendation is to prioritise keeping the ball in play."
        confidence = "low"

    return RecommendationResponse(
        recommendation=recommendation,
        reasoning=reasoning,
        confidence=confidence,
    )