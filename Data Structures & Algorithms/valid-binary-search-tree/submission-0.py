# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity - O(n)
# Space complexity - O(h)

class Solution:
    def isValid(self, low, node, high):
            if not node:
                # If we got this far to a leaf
                # it has to be valid
                return True
            if not (low < node.val < high):
                return False
            # Left subtree - upper bound becomes the root, keep low as lower bound
            # Right subtree - lower bound becomes the root, keep high as upper bound
            return (self.isValid(low,node.left, node.val) and self.isValid(node.val, node.right, high))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(float('-inf'), root, float('inf'))