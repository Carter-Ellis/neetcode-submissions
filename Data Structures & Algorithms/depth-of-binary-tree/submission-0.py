# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        def traverse(curr, depth):
            if not curr:
                return 0
            depth += 1
            maxDepth[0] = max(maxDepth[0], depth)
            traverse(curr.left, depth)
            traverse(curr.right, depth)
        traverse(root, 0)
        return maxDepth[0]
