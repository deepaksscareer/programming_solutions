def get_all_total_pair_match_sum(list_number: list, total_sum: int):
    """
    For the given list, check if any 2 number match the total
    :param list_number:
    :param total_sum:
    :return:
    """

    # Edge condition
    # If the list is empty return False
    if not list_number:
        return False

    # Sort list
    list_number.sort()

    list_matches = []

    left = 0
    right = len(list_number) - 1

    # Move left and right
    while left < right:

        current_sum = list_number[left] + list_number[right]

        # Return condition
        if current_sum == total_sum:
            list_matches.append((list_number[left], list_number[right]))

            # Eliminate duplicates and move left or right
            match_left = list_number[left]
            match_right = list_number[right]

            # If it matches move right for left
            while left < right and list_number[left] == match_left:
                left += 1

            # If it matches move right for left
            while left < right and list_number[right] == match_right:
                right -= 1

        # If left is less than total, then move right
        elif current_sum < total_sum:
            left += 1

        # Move the right part
        else:
            right -= 1

    return list_matches


