class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                # No opening bracket to match this closing bracket
                if not stack:
                    return False

                opening = stack.pop()

                # Check whether the types match
                if opening != pairs[bracket]:
                    return False

        # Valid only if no opening brackets remain
        return len(stack) == 0
