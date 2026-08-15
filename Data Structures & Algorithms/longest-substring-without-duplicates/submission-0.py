class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        # Store the character and the index
        hashmap = {}
        for right in range(len(s)):
            # If already in the hashmap
            if s[right] in hashmap:
                # Only update left if the new character is after the current left
                left = max(left, hashmap[s[right]] + 1)
            # Update right
            hashmap[s[right]] = right
            # Update max length
            max_length = max(max_length, (right-left +1))
        return max_length

