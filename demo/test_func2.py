import numpy as np
import func as fc
import pytest


@pytest.mark.parametrize(
    "myinput", "myref", [(1, np.pi), (0, 0), (2.1, np.pi * 2.1 ** 2)]
)
def test_area_circ(myinput, myref):
    assert fc.area_circ(myinput) == myref
