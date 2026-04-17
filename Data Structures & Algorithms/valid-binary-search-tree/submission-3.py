# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxVal = -1001
        
        def dfs(curr: Optional[TreeNode]) -> bool:

            nonlocal maxVal
            if not curr:
                return True
            
            if not dfs(curr.left):
                return False

            if curr.val <= maxVal:
                return False
            maxVal = curr.val

            if not dfs(curr.right):
                return False

            return True

        return dfs(root)