# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(curr, total):
            if not curr:
                return 0
            total += max(traverse(curr.left, total), traverse(curr.right, total)) + 1
            return total
        total = 0
        return traverse(root, total)

            
