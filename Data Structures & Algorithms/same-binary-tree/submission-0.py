# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(curr1, curr2) -> bool:
            print("HOLa")
            if curr1 == None and curr2 != None:
                print("yo")
                return False
            elif curr1 != None and curr2 == None:
                print("HUllo")
                return False
            elif curr1 == None and curr2 == None:
                return True
            if curr1.val != curr2.val:
                print("wrong")
                return False
            if not rec(curr1.left, curr2.left):
                print(curr1.left)
                print(curr2.left)
                print("left")
                return False
            if not rec(curr1.right, curr2.right):
                print("right")
                return False
            return True
        return rec(p,q)