import pytest

from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2], 1) == [2]
    assert arrs.my_slice([1, 2], 2) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], 0, 3) == [1, 2, 3]
    assert arrs.my_slice([1], 4, 3) == []
    assert arrs.my_slice(["1", "4"], -15, -2) == []
    assert arrs.my_slice(["1", [1, 2, 3], 3], 0, 4) == ['1', [1, 2, 3], 3]
    assert arrs.my_slice([], 1, ) == []


def test_get_val():
    assert dicts.get_val({"dog": "puppy", "cat": "kitty", "1": "23", "4": "56"}, "4", 'git') == "56"
    assert dicts.get_val({"dog": "puppy", "cat": "kitty", "1": "23", "4": "56"}, "dog", 'git') == "puppy"
    assert dicts.get_val({"dog": "puppy", "cat": "kitty", "1": "23", "4": "56"}, 4, 'git') == "git"
    assert dicts.get_val({}, 4, 'git') == "git"
