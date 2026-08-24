class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = set(nums)
        sequence_length = 0
        # The start of the sequence is the element that does not have (n-1) in it
        # After that, what do we do? Keep iterating through the counter while key in counter.keys()
        # Then compare max length and update
        for key in counter:
            if (key-1) not in counter:
                cur = key
                length = 1
                while (cur + 1)in counter:
                    cur += 1
                    length += 1
                sequence_length = max(sequence_length, length)

        return sequence_length
        

            
        