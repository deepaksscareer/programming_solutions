def is_both_string_anagram(string_1: str, string_2: str):
    # Edge cases

    # If the length is different then raise false
    if len(string_1) != len(string_2):
        return False

    if string_1 == "":
        return True

    update_string_1 = string_1.lower()
    update_string_2 = string_2.lower()

    char_mapping = {}

    # Make the 1st string dictionary
    for letter in update_string_1:

        if letter in char_mapping:
            char_mapping[letter] += 1
        else:
            char_mapping[letter] = 1

    # Check the 2nd string vs the 1st dictionary
    for letter in update_string_2:

        # Edge cases
        if letter not in char_mapping:
            return False

        # Reduce count
        current_count = char_mapping[letter]

        # If the count is 0, then remove key
        if current_count == 1:
            char_mapping.pop(letter)
        else:
            # Else we will reduce by 1
            char_mapping[letter] = current_count - 1

    # If it is not empty, then return error
    return len(char_mapping.keys()) == 0
