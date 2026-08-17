import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string using regex
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        print(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -=1
        return True
        