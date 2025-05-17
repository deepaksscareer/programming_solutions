def check_pair_exists_to_sum(list_number: list, total_sum: int):
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

    left = 0
    right = len(list_number) - 1

    # Move left and right
    while left < right:

        current_sum = list_number[left] + list_number[right]

        # Return condition
        if current_sum == total_sum:
            return True

        # If left is less than total, then move right
        elif current_sum < total_sum:
            left += 1

        # Move the right part
        else:
            right -= 1

    return False


