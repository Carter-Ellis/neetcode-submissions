"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyHead = Node(0)
        dummy, curr = dummyHead, head
        random_nodes = {}

        #Create copied list with populating random_nodes dictionary
        while curr:
            new_node = Node(curr.val)
            random_nodes[curr] = new_node
            dummy.next = new_node
            dummy = new_node
            curr = curr.next
        
        new_head, curr = dummyHead.next, head
        copy_curr = new_head

        #Populate random nodes in copied list
        while curr:
            if curr.random:
                copy_curr.random = random_nodes.get(curr.random, None)
            curr = curr.next
            copy_curr = copy_curr.next

        return new_head