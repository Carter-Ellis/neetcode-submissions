# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(curr: Optional[TreeNode], k: int) -> int:
            nonlocal count
            if not curr:
                return -1
            
            res = dfs(curr.left, k)
            if res != -1:
                return res

            count += 1

            if count == k:
                return curr.val


            res = dfs(curr.right, k)
            return res
        return dfs(root, k)