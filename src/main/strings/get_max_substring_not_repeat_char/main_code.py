from collections import OrderedDict
from src.main.logging_module_test.check_logging import get_logger

logger = get_logger()

def get_max_substring_not_repeat_char(message: str):

    # Edge cases
    # If length is 0, then return
    if len(message) == 0:
        return 0

    # Lower case should be consider??

    logger.info(f"Current text: {message}")

    max_non_repeat = 0

    # Pointers
    left = 0
    repeat_set = OrderedDict()

    for right in range(len(message)):

        current_char = message[right]

        if current_char in repeat_set.keys():
            repeat_set.pop(current_char)

            # Reset the sliding window pointer
            left = right

        # Add the key to ordered set
        repeat_set[current_char] = True

        logger.info(f"For current text: {message[0:right+1]}, the set: {repeat_set}")

        max_non_repeat = max(max_non_repeat, right - left + 1)

    return max_non_repeat

print(get_max_substring_not_repeat_char(message="abcabcbb"))