def direction(facing, turn):
    direction_degrees = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315
    }
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return directions[(direction_degrees[facing] + turn) % 360 // 45]