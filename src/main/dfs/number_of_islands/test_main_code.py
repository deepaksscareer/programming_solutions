import pytest

from src.main.dfs.number_of_islands.main_code import get_no_of_island


def test_empty_island():

    grid = [
    ]
    result = get_no_of_island(grid=grid)
    assert result == 0

def test_valid_island():

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = get_no_of_island(grid=grid)
    assert result == 3
