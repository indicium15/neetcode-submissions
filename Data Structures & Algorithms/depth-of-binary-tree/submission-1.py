# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        length = 0
        # Have to wrap in an array
        queue = deque([root])
        while len(queue) > 0:
            for i in range(len(queue)):
                pop = queue.popleft()
                if pop.left:
                    queue.append(pop.left)
                # This can't be elif otherwise it will only run
                # if left is not there
                if pop.right:
                    queue.append(pop.right)
            length += 1
        return length

        