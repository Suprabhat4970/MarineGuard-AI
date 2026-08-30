def calculate_route_risk(wind_speed, wave_height, visibility, weather_condition):

    risk_score = 0

    if wind_speed > 40:
        risk_score += 35
    elif wind_speed > 20:
        risk_score += 20

    if wave_height > 4:
        risk_score += 35
    elif wave_height > 2:
        risk_score += 20

    if visibility < 2:
        risk_score += 25
    elif visibility < 5:
        risk_score += 15

    weather = weather_condition.lower()

    if weather == "storm":
        risk_score += 30
    elif weather == "rain":
        risk_score += 10

    if risk_score <= 30:
        risk_level = "LOW"
    elif risk_score <= 60:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }