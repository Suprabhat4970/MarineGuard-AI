def calculate_route_risk(wind_speed, wave_height, visibility, weather_condition):

    risk_score = 0

    # WIND
    if wind_speed > 40:
        risk_score += 35
        wind_risk = "High"
    elif wind_speed > 20:
        risk_score += 20
        wind_risk = "Moderate"
    else:
        wind_risk = "Low"

    # WAVES
    if wave_height > 4:
        risk_score += 35
        wave_risk = "High"
    elif wave_height > 2:
        risk_score += 20
        wave_risk = "Moderate"
    else:
        wave_risk = "Low"

    # VISIBILITY
    if visibility < 2:
        risk_score += 25
        visibility_risk = "Poor"
    elif visibility < 5:
        risk_score += 15
        visibility_risk = "Moderate"
    else:
        visibility_risk = "Good"

    # WEATHER
    weather = weather_condition.lower()

    if weather == "storm":
        risk_score += 30
        weather_risk = "Storm"
    elif weather == "rain":
        risk_score += 10
        weather_risk = "Rain"
    else:
        weather_risk = "Clear"
    if risk_score <= 30:
        risk_level = "LOW"
    elif risk_score <= 60:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

        return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risk_factors": {
            "wind": wind_risk,
            "waves": wave_risk,
            "visibility": visibility_risk,
            "weather": weather_risk
        }
    }