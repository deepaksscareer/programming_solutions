from collections import Counter

def are_anagrams(s1: str, s2: str):
    update_first_string = s1.lower()
    update_second_string = s2.lower()

    return Counter(update_first_string) == Counter(update_second_string)


print(f"Are anagrams : 'silent' and 'listen' : {are_anagrams(s1='silent', s2='listen')}")

print(Counter('silent'))