from src.main.two_pointers.all_total_sum_value_equal_pair.main_code import get_all_total_pair_match_sum


def test_list_pair_matches():

    input_list = [1, 2, 3, 4, 4, 6, 5, 7]
    match_list = [(1, 7), (2, 6), (3, 5), (4, 4)]

    result = get_all_total_pair_match_sum(list_number=input_list, total_sum=8)
    assert result == match_list


def test_list_pair_no_match():
    input_list = [1, 2, 3, 4, 4, 6, 5, 7]
    match_list = []

    result = get_all_total_pair_match_sum(list_number=input_list, total_sum=50)
    assert result == match_list

# Check if sum is negative will it work??
