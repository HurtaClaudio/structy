# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0

  while current_1 or current_2:
    if current_1 and not current_2:
      tail.next = current_1
      break
    elif current_2 and not current_1:
      tail.next = current_2
      break
      
    if count % 2 == 0:
      tail.next = current_2
      tail = current_2
      current_2 = current_2.next
      count += 1
    else:
      tail.next = current_1
      tail = current_1
      current_1 = current_1.next
      count += 1

  return head_1
