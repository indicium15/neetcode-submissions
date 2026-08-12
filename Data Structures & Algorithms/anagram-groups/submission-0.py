from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map of counters?
        counter_list = []
        ans = []
        for i in range(len(strs)):
            counter = Counter(strs[i])
            if counter in counter_list:
                index = counter_list.index(counter)
                ans[index].append(strs[i])
            else:
                ans.append([])
                ans[-1].append(strs[i])
                counter_list.append(counter)
        print(ans)
        return ans
