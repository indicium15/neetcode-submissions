from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sequence_length = 0
        # The start of the sequence is the element that does not have (n-1) in it
        # After that, what do we do? Keep iterating through the counter while key in counter.keys()
        # Then compare max length and update
        for key in counter.keys():
            if (key-1) not in counter.keys():
                cur = key
                length = 0
                while cur in counter.keys():
                    cur += 1
                    length += 1
                sequence_length = max(sequence_length, length)

        return sequence_length
        

            
        