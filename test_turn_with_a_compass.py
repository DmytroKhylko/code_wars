import pytest
from turn_with_a_compass import direction

@pytest.mark.parametrize("test_input, expected", [(("N", 90), "E"), (("W", -90), "S"), (("N", -405), "NW")])
def test_direction_valid_input(test_input, expected):
    assert direction(test_input[0], test_input[1]) == expected

@pytest.mark.parametrize("test_input", [(["N"], 90), ("N", "90")])
def test_direction_type_error(test_input):
    with pytest.raises(TypeError):
        assert direction(test_input[0], test_input[1])

@pytest.mark.parametrize("test_input", [("H", 90), ("N", 2000), ("N", 36)])
def test_direction_incorrect_inpput(test_input):
    with pytest.raises(AssertionError):
        assert direction(test_input[0], test_input[1])