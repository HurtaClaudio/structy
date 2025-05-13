# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  current = head
  result = []

  if head is None:
    return []
  
  #do-while
  result.append(current.val)
  while current.next:
    current = current.next
    result.append(current.val)

  return result