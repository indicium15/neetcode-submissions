class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # If the stack is empty or 
            # Top of the stack has a greater value than the temperatures
            # Add it to the stack
            if len(stack) == 0 or stack[-1][1] > temperatures[i]:
                stack.append((i, temperatures[i]))
            else:
                # At this point it is already lower than current
                # But this has to be a while loop because the same value
                # Can be used for multiple responses
                while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                    data = stack.pop()
                    index = data[0]
                    diff = i - index
                    # We need to insert the value at the index the date was recorded
                    result[index] = diff
                # Append the new value to the stack for the next temperature
                stack.append((i, temperatures[i]))
        return result

            
        