# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        newQueue = deque()
        res = [[root.val]]
        sublist = []

        while queue:
            curr = queue.popleft()
            left, right = curr.left, curr.right
            if left:
                sublist.append(left.val)
                newQueue.append(left)
            if right:
                sublist.append(right.val)
                newQueue.append(right)
            if not queue:
                if not sublist:
                    break
                queue = newQueue
                res.append(sublist)
                newQueue = deque()
                sublist = []
        return res