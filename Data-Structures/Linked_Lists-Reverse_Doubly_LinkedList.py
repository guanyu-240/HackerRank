"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if not head: return head
    ptr =  head
    tmp = None
    while ptr:
        if not ptr.next: head = ptr
        tmp = ptr.prev
        ptr.prev = ptr.next
        ptr.next = tmp
        ptr = ptr.prev
    return head
