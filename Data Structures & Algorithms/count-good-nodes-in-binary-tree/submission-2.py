# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(curr: TreeNode, count: int, maxVal: int) -> int:
            count = 0
            if not curr:
                return 0
            if curr.val >= maxVal:
                count = 1
            maxVal = max(maxVal, curr.val)
            return traverse(curr.left, count, maxVal) + traverse(curr.right, count, maxVal) + count
        return traverse(root, 0, -101)