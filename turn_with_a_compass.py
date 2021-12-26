def direction(facing: str, turn: int):
    if not isinstance(facing, str):
        raise TypeError("facing parameter must be of type str")
    if not isinstance(turn, int): 
        raise TypeError("turn parameter must be of type int")

    assert -1080 <= turn <= 1080 and turn % 45 == 0, "turn parameter must be in range [-1080, 1080] and multiple of 45" 

    directions = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
    assert facing in directions, f"facing parameter must one of the following: {directions}"

    direction_degrees = dict(zip(directions, [0, 45, 90, 135, 180, 225, 270, 315]))

    return directions[(direction_degrees[facing] + turn) % 360 // 45]
