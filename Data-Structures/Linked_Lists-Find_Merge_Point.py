"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    offset = 0
    ptr = headA
    while ptr:
        ptr = ptr.next
        offset += 1
    ptr = headB
    while ptr:
        ptr = ptr.next
        offset -= 1
    if offset > 0: ptr,ptr_other = headA,headB
    else: ptr,ptr_other = headB,headA
    offset = abs(offset)
    while offset > 0: 
        ptr = ptr.next
        offset -= 1
    while ptr and ptr_other:
        if ptr.data == ptr_other.data: return ptr.data
        ptr,ptr_other = ptr.next,ptr_other.next
    return None
