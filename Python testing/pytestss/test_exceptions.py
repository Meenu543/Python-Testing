import pytest

'''
--> Errors can be raised using 'pytest.raises(Type of ERROR)'
'''


def divide(input1, input2):
    return input1 / input2


def test_divide():
    assert divide(48, 2) == 24


def test_divide_by_zero():
    # assert divide(48, 0) == 24 raises error
    with pytest.raises(ZeroDivisionError):
        divide(48, 0)


def test_divide_by_string():
    # assert divide(48, '2') == 24
    with pytest.raises(TypeError):
        divide(48, '2')
