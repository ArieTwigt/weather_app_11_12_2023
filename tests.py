import pytest

def calc_size(length, width):

    # cast to the right types
    length_float = float(length)
    width_float = float(width)

    # check if the values are positive
    if length_float < 0 or width_float < 0:
        raise ValueError("The values cannot be negative")

    # calculate size
    size = width_float * length_float

    return size


# execute the tests
def test_calc_size():
    assert calc_size(4, 4) == 16
    assert calc_size("5", 4) == 20


def test_not_negative():
    with pytest.raises(ValueError):
        calc_size(-4, 10)