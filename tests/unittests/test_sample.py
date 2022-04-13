
from pickle import FALSE, TRUE


def is_lower_or_equal_than_10(x):
    if x <= 10:
        return TRUE
    return FALSE

# def is_lower_or_equal_than_10(x):
#     if x == 10:
#         return TRUE
#     return FALSE


def test_10():
    assert is_lower_or_equal_than_10(10) == TRUE

def test_11():
    assert is_lower_or_equal_than_10(11) == FALSE

def test_12():
    assert is_lower_or_equal_than_10(12) == FALSE

def test_9():
    assert is_lower_or_equal_than_10(9) == TRUE

