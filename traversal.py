#! /usr/local/bin/python33

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

root = Node('F')
root.left = Node('B', Node('A'), Node('D', Node('C'), Node('E')))
root.right = Node('G', None, Node('I', Node('H')))

def pre_order_traversal(node):
  if not node:
    return []

  result = []
  result.append(node.val)
  result += pre_order_traversal(node.left)
  result += pre_order_traversal(node.right)

  return result

print('pre order traversal')
arr = pre_order_traversal(root)
print(arr)

def level_order_traversal(node):
  result = []
  if not node:
    return

  queue = [node]
  while len(queue):
    level = []
    queue2 = []
    for item in queue:
      level.append(item.val)
      if item.left:
        queue2.append(item.left)
      if item.right:
        queue2.append(item.right)

    result.append(level)
    queue = queue2
  return result


print('level order traversal')
arr = level_order_traversal(root)
print(arr)

def maxDepth(root):
  """
  buttom up, get the max depth of a tree
  """
  if not root:
      return 0
  left = maxDepth(root.left)
  right = maxDepth(root.right)
  return max(left, right) + 1
