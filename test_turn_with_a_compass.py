import pytest
from turn_with_a_compass import direction

def test_direction():
    assert direction("N", 90) == "E"

    with pytest.raises(TypeError):
        assert direction(["N"], 90)
        assert direction("N", "90")

    with pytest.raises(AssertionError):
        assert direction("H", 90)
        assert directoin("N", 2000)
        assert direction("N", 36)