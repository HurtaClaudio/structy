# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  if head.val == target:
    return True
  if head.next is None:
    return False
  
  return linked_list_find(head.next, target)
