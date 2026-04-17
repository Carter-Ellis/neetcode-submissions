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
        level = 0
        result = []
        
        while len(queue) > 0:
            tempList = []
            for i in range(len(queue)):
                print(len(queue))
                print(queue)
                curr = queue.popleft()
                tempList.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(tempList)
            level += 1
        return result
        