import pytest
from main import for_else_check_odd_num


def test_for_else():
    result = for_else_check_odd_num(3)
    assert result
    result = for_else_check_odd_num(4)
    assert not result


def test_dict_get():
    my_dict = {'a': 1, 'b': 2}
    assert my_dict.get('a')
    assert not my_dict.get('c')  # will default return None if key is not found in dict


def test_complex_num():
    assert 1j * 2j == -2
    assert (3 + 4j) * (2 + 3j) == (-6 + 17j)
