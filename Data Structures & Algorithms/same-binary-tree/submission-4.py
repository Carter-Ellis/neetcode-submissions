# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(curr1, curr2) -> bool:
            if not curr1 and not curr2:
                return True
            if curr1 and curr2 and curr1.val == curr2.val:
                return rec(curr1.left, curr2.left) and rec(curr1.right, curr2.right)       
            return False
        return rec(p,q)