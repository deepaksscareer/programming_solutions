# Main class
# Testing scenarios
import pytest

from src.main.stack_medium_question.balanced_parantheses.balanced_parantheses_check import CheckBalancedParan

def test_empty_parantheses_check():
    # TODO document why this method is empty
    char_check = CheckBalancedParan()
    result = char_check.add_code(expression="")
    assert result


def test_invalid_parantheses_check():
    # TODO document why this method is empty
    char_check = CheckBalancedParan()
    result = char_check.add_code(expression="{[}]")
    assert not result


def test_valid_parantheses_check():
    # TODO document why this method is empty
    char_check = CheckBalancedParan()
    result = char_check.add_code(expression="[({})]")
    assert result
