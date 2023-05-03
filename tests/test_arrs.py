

import pytest

from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


a = [1, 2, 3, 4]


@pytest.fixture
def arrs_fixture():
    return [1, 2, 3, 4, 5, 6]

def test_slice(arrs_fixture):
    assert arrs.my_slice(arrs_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(arrs_fixture, -1, 3) == []
    assert arrs.my_slice(arrs_fixture, 0, 3) == [1, 2, 3]
    assert arrs.my_slice([1], 4, 3) == []
    assert arrs.my_slice(["1", "4"], -15, -2) == []
    assert arrs.my_slice(["1", [1, 2, 3], 3], 0, 4) == ['1', [1, 2, 3], 3]
    assert arrs.my_slice([], 1, ) == []


@pytest.fixture
def get_fixture():
    return {"dog": "puppy", "cat": "kitty", "1": "23", "4": "56"}
def test_get_val(get_fixture):
    assert dicts.get_val(get_fixture, "4", 'git') == "56"
    assert dicts.get_val(get_fixture, "dog", 'git') == "puppy"
    assert dicts.get_val(get_fixture, 4, 'git') == "git"
    assert dicts.get_val({}, 4, 'git') == "git"
