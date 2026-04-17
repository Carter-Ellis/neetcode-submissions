# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#   Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path,
#   where a path is a sequence of nodes where each pair of adjecent nodes has an edge connecting them.
#
#   Notes:
#       - A path does not need to include the root
#       - A path can be linked from a left subtree to the right subtree.
#       - negative nodes could hurt the path.
#       - No node cannot appear twice in a path
#
#

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001

        def dfs(curr: Optional[TreeNode]) -> int:
            nonlocal res
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            res = max(res, left + right + curr.val)
            return max(left + curr.val, right + curr.val, curr.val, 0)
        dfs(root)
        return res
