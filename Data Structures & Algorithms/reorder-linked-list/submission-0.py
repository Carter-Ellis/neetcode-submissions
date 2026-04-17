# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = []
        curr = head
        
        while curr:
            nodeList.append(curr)   
            curr = curr.next
        i, j = 0, len(nodeList) - 1
        leftNode = True
        while i < j:
            if leftNode:
                nodeList[i].next = nodeList[j]
                i += 1
                leftNode = False
                if i == j:
                    nodeList[j].next = None
            else:
                nodeList[j].next = nodeList[i]
                j -= 1
                leftNode = True
                if i == j:
                    nodeList[i].next = None
