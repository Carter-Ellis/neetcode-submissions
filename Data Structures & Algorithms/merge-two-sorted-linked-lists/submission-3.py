# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, newList = list1, list2, None
        newListHead = None
        if not curr1:
            return curr2
        if not curr2:
            return curr1
        while curr1 and curr2:
            
            if curr1.val <= curr2.val:                
                if newList is None:
                    newList = curr1
                    newListHead = newList
                else:
                    newList.next = curr1
                    newList = newList.next
                curr1 = curr1.next
            else:
                if newList is None:
                    newList = curr2
                    newListHead = newList
                else:                  
                    newList.next = curr2
                    newList = newList.next            
                curr2 = curr2.next
        if curr1:
            while curr1:
                newList.next = curr1
                newList = newList.next
                curr1 = curr1.next
        if curr2:
            while curr2:
                newList.next = curr2
                newList = newList.next
                curr2 = curr2.next
        return newListHead