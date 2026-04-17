# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def isSameTree(curr, subCurr):
            if not curr and not subCurr:
                return True
            if not curr or not subCurr or curr.val != subCurr.val:
                return False
            return isSameTree(curr.left, subCurr.left) and isSameTree(curr.right, subCurr.right)

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
