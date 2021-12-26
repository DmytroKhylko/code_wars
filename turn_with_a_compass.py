def direction(facing: str, turn: int):
    assert type(facing) is str, "facing parameter must be of type str"
    assert type(turn) is int, "turn parameter must be of type int"
    assert turn <= 1080 and turn >= -1080, "turn parameter must be in range [-1080, 1080]" 
    assert turn % 45 == 0, "turn parameter must be multiple of 45"
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
    assert facing in direction_degrees.keys(), "facing parameter must one of the following: N, NE, E, SE, S, SW, W, NW"
    return list(direction_degrees.keys())[(direction_degrees[facing] + turn) % 360 // 45]

print(direction("N", 1079))