# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
    if root.left is None and root.right is None:
        return root.val

    max_child_sum = float('-inf')

    if root.left:
        max_child_sum = max(max_child_sum, max_path_sum(root.left))

    if root.right:
        max_child_sum = max(max_child_sum, max_path_sum(root.right))

    return root.val + max_child_sum
