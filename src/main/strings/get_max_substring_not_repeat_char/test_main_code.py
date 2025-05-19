from src.main.strings.get_max_substring_not_repeat_char.main_code import get_max_substring_not_repeat_char


def test_substring_case_1():

    input_string = "abcabcd"

    result = get_max_substring_not_repeat_char(message=input_string)

    assert result == 3


def test_substring_case_2():
    input_string = "abbc"

    result = get_max_substring_not_repeat_char(message=input_string)

    assert result == 2

