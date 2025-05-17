
from src.main.two_pointers.pair_numbers_equal_value.main_code import check_pair_exists_to_sum


def test_true_sum():
    input_list = [1, 2, 3, 6]
    result = check_pair_exists_to_sum(list_number=input_list, total_sum=5)

    assert result


def test_false_sum():
    input_list = [1, 2, 3, 6]
    result = check_pair_exists_to_sum(list_number=input_list, total_sum=20)

    assert not result

# Check if sum is negative will it work??

