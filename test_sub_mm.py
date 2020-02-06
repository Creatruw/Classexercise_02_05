import pytest
from sub_mm import sub
from sub_mm import fm


@pytest.mark.parametrize("a, b, expected, result", [
    (3, 2, 1, True),
    (10, 9, 1, True),
    (5, 5, 1, False),
    (3.4, 3.2, pytest.approx(0.2), True),
])
def test_sub_parametrize(a, b, expected, result):
    answer = sub(a, b)
    assert result == (expected == answer)


@pytest.mark.parametrize("a, min1, max1, result", [
    ([1, 2, 3, 4, 5, 6], 1, 6, True),
    ([3, 4, 6, 7, 8, 10], 3, 10, True),
    ([4, 5, 6, 7, 8, 10.1, 10], 4, 10.1, True),
    ([1, 3, 5, 7, 9], 9, 1, False),
])
def test_fm_parametrize(a, min1, max1, result):
    min2, max2 = fm(a)
    assert result == (min2 == min1 and max2 == max1)
