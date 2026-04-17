# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1, curr2 = l1, l2
        dummyHead = ListNode()
        dummy = dummyHead

        while curr1 or curr2:
            total = 0
            if curr1 and not curr2:
                total = curr1.val + carry
            elif not curr1 and curr2:
                total = curr2.val + carry
            else:
                total = curr1.val + curr2.val + carry

            if total >= 10:
                carry = 1
                total %= 10
            else:
                carry = 0
            
            dummy.next = ListNode(total)
            dummy = dummy.next
            
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry == 1:
            dummy.next = ListNode(1)
        
        return dummyHead.next
            