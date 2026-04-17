# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Calculate length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        #Calculate position of node to remove
        position = length - n
        curr = head
        prev = None
        #Traverse to specific node
        for i in range(position):
            prev = curr
            curr = curr.next
        
        #Remove the node from the list
        temp = curr.next
        if prev:
            prev.next = temp
        
        #If removed node is the head
        if curr == head:
            head = temp

        return head