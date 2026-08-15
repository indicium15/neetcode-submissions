from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = Counter(s1)
        target_matches = len(count)
        matches = 0
        left = 0
        right = len(s1)
        
        for i in range(left, right):
            count[s2[i]] -= 1
            if count[s2[i]] == 0:
                matches += 1

        while True:

            if matches == target_matches:
                return True

            if right == len(s2):
                break

            # This guy is leaving the window
            # So the count should increase
            # Matches should decrease
            if count[s2[left]] == 0:
                matches -= 1
            count[s2[left]] += 1
            left+=1

            # This guy is entering the window
            # right is already the character waiting to enter
            count[s2[right]] -= 1
            if count[s2[right]] == 0:
                matches += 1
            right+=1
            
        return False