# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(curr: Optional[TreeNode], count) -> None:
            if not curr:
                return
            count += 1
            self.maxD = max(self.maxD, count)
            dfs(curr.left, count)
            dfs(curr.right, count)

        dfs(root, 0)
        return self.maxD