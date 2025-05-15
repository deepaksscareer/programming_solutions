from collections import deque

# Main class
class CheckBalancedParan:

    def __init__(self):
        self.character_stack = deque()

        self.char_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def add_code(self, expression: str):

        # Edge condition
        self.character_stack.clear()

        for char in expression:

            if char in self.char_map.values():
                self.character_stack.append(char)

            if char in self.char_map.keys():

                # If the top of stack matches the given char, then remove from top else, it is a
                if self.character_stack[-1] != self.char_map[char]:
                    print(f"The message {expression} is unbalanced")
                    return False
                else:
                    self.character_stack.pop()

        # If the stack is empty, then we are good
        if len(self.character_stack) == 0:
            print(f"The message {expression} is balanced")
            return True
        else:
            print(f"The message {expression} is unbalanced")
            return True

if __name__ == "__main__":

    check_balance = CheckBalancedParan()

    check_balance.add_code(expression="{}[]")

    check_balance.add_code(expression="{[]}")

    check_balance.add_code(expression="{[}]")