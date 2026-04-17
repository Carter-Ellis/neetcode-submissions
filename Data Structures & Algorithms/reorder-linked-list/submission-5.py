# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head.next:
            return

        length = 0
        curr = head
        #Determine length of linked list
        while curr:
            length += 1
            curr = curr.next

        def reverse_half(head: Optional[ListNode], dummyHead: ListNode, length) -> ListNode:
            
            curr = head
            #Get to start position
            for i in range((length // 2) - 1):
                curr = curr.next
            
            #Remove the halfway link
            temp = curr.next
            curr.next = None
            curr = temp

            #Reverse remaining links
            
            temp = None
            while curr:
                temp = curr.next
                curr.next = dummyHead
                dummyHead = curr
                curr = temp

            return dummyHead
        
        dummyHead = reverse_half(head, ListNode(), length)

        #Connect the linked lists
        curr = head
        temp = None
        while curr:
            temp = curr.next
            curr.next = dummyHead
            curr = temp
            temp = dummyHead.next

            # Check for odd linked lists
            if not curr and temp and temp.next:
                temp.next = None
            else:
                dummyHead.next = curr

            
            dummyHead = temp
            
            









