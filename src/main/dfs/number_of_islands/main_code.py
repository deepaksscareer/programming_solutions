from typing import List
import logging

def get_no_of_island(grid: List[List[str]]):
    """
    For the given input message, get the no of islands
    :param message:
    :return: Get the no of islands
    """

    # Edge case
    # If grid is empty, then raise an error
    if not grid:
        return 0

    no_rows = len(grid)
    no_columns = len(grid[0])

    no_islands = 0
    list_visits = set()
    def _check_node(r, c):

        # If the edge of is reached, then return done
        if r < 0 or r >= no_rows or c < 0 or c >= no_columns or (r, c) in list_visits or grid[r][c] == "0":
            return

        # This means that the value is 1 and adding that this has been traversed
        list_visits.add((r, c))

        # go to the left
        _check_node(r - 1, c)

        # go to the right
        _check_node(r + 1, c)

        # go to the up
        _check_node(r, c + 1)

        # go the down
        _check_node(r, c - 1)

    # Loop through the rows
    for r in range(no_rows):

        # Loop through the columns:
        for c in range(no_columns):

            if grid[r][c] == "1" and (r, c) not in list_visits:
                _check_node(r, c)
                no_islands += 1

    return no_islands

if __name__ == "__main__":

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(get_no_of_island(grid=grid))
