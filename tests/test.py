import pytest
from main import for_else_check_odd_num, incorrect_default_list_value, correct_default_list_value


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


def test_str_methods():
    assert "level".count('l') == 2
    assert "rich".endswith("ch")
    assert "level".find('e') == 1
    assert "1 + 2 = {0}".format(3) == "1 + 2 = {a}".format(a='3') == "1 + 2 = 3"
    assert "apple".isalpha()
    assert not "index1".isalpha()
    assert "3456".isnumeric()
    assert "black".upper() == "BLACK"
    assert "this".replace('is', 'at') == "that"
    assert "a,b".split(',') == ['a', 'b']
    assert "idea".startswith("id")
    assert "    inside    ".strip() == "inside"


def test_default_list_value():
    assert incorrect_default_list_value(1) == [1]
    assert incorrect_default_list_value(2) == [1, 2]
    assert correct_default_list_value(1) == [1]
    assert correct_default_list_value(2) == [2]


def test_lambda_expression():
    # sort list by first character using lambda_expression
    fruits = ['watermelon', 'orange', 'banana', 'apple']
    fruits.sort(key=lambda x: x[0])
    assert fruits == ['apple', 'banana', 'orange', 'watermelon']


def test_list_methods():
    init_list = [i for i in range(3)]
    assert init_list.index(1) == 1
    init_list.insert(1, 3)
    assert init_list == [0, 3, 1, 2]
    assert init_list.pop() == 2
    assert init_list == [0, 3, 1]
    init_list.sort(reverse=True)
    assert init_list == [3, 1, 0]
    init_list.reverse()
    assert init_list == [0, 1, 3]
    copy_list = init_list.copy()
    init_list.clear()
    assert init_list == []
    assert copy_list == [0, 1, 3]
