class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_count = Counter(s)
        # print(s_count)
        t_count = Counter(t)
        return s_count == t_count