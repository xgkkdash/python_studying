import pytest
from main import for_else_check_odd_num


def test_for_else():
    result = for_else_check_odd_num(3)
    assert result
    result = for_else_check_odd_num(4)
    assert not result
