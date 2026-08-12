from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = []
        res = []
        for s in strs:
            counter = Counter(s)
            print(s)
            print(counters)
            if counter in counters:
                if res[counters.index(counter)]:
                    res[counters.index(counter)].append(s)
                else:
                    res[counters.index(counter)] = [s]
            else:
                res.append([s])
                counters.append(counter)
        return res
            
