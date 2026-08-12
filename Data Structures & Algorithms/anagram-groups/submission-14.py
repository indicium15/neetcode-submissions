from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map - the key is the sorted value of the string 
        anagrams = {}
        for s in strs:
            # Compute value of the sorted string
            key = "".join(sorted(s))
            # Append if it already exists
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        return list(anagrams.values())