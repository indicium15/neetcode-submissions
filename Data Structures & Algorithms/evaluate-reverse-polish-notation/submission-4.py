class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                top_1 = stack.pop()
                top_2 = stack.pop()
                if token == "+":
                    stack.append(top_2 + top_1)
                elif token == "/":
                    stack.append(int(top_2 / top_1))
                elif token == "*":
                    stack.append(top_2 * top_1)
                elif token == "-":
                    stack.append(top_2 - top_1)
            else:
                print
                stack.append(int(token))
        return int(stack[-1])
                
                