# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                # The answer is in the right subtree if both are greater than the current value
                return self.lowestCommonAncestor(root.right, p, q)
                # The answer is in the left subtree if both are lesser than the current value
            elif p.val < cur.val and q.val < cur.val:
                # When we cannot move any lower, we are at the lowest common ancestor because there is no more "splitting"
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return cur