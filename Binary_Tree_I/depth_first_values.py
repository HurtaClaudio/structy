# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  stack = [root]
  visited = []

  while stack:
    current = stack.pop()
    if not current:
      continue
    visited.append(current.val)
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return visited