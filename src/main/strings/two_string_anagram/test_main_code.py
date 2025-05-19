from src.main.strings.two_string_anagram.main_code import is_both_string_anagram


def test_valid_anagram():
    string_1 = "listen"
    string_2 = "SIlent"

    result = is_both_string_anagram(string_1=string_1, string_2=string_2)

    assert result

def test_invalid_anagram():
    string_1 = "listen"
    string_2 = "SIlented"

    result = is_both_string_anagram(string_1=string_1, string_2=string_2)

    assert not result


def test_invalid_anagram_blank_param():
    string_1 = ""
    string_2 = ""

    result = is_both_string_anagram(string_1=string_1, string_2=string_2)

    assert result

def test_invalid_anagram_second():
    string_1 = "listen"
    string_2 = "dramas"

    result = is_both_string_anagram(string_1=string_1, string_2=string_2)

    assert not result
