from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    assert sum(split_integer(10, 2)) == 10


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(20, 4) == [5, 5, 5, 5]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(15, 1) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(17, 3) == [5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
