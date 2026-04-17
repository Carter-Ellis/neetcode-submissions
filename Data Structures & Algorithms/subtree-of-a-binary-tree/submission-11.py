# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkTree(curr, currSub) -> bool:
            if not curr:
                return False
            if isValidSubtree(curr, currSub):
                return True
            else:
                return checkTree(curr.left, currSub) or checkTree(curr.right, currSub)

        def isValidSubtree(curr, currSub) -> bool:
            if not curr and not currSub:
                return True
            if curr and not currSub:
                return False
            if not curr and currSub:
                return False
            if curr.val != currSub.val:
                return False
            return isValidSubtree(curr.left, currSub.left) and isValidSubtree(curr.right, currSub.right)
        
        return checkTree(root, subRoot)