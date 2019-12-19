#! /usr/local/bin/python3

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return self.val

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


def isSymmetric(root):
  if not root:
    return True
  list = [root.left, root.right]
  while len(list):
    item = list.pop(0)
    otherItem = list.pop(0)
    if not item and not otherItem:
        continue
    if not item or not otherItem:
        return False
    if item.val != otherItem.val:
        return False
    list += [item.left, otherItem.right, item.right, otherItem.left]

  return True

def isSymmetric_rec(root):
  if not root:
    return True
  return isMirror(root.left, root.right)

def isMirror(item1, item2):
  if not item1 and not item2:
      return True
  if not item1 or not item2:
      return False
  return (item1.val == item2.val and
          isMirror(item1.left, item2.right) and
          isMirror(item1.right, item2.left))

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    def ser(node, string):
        if not node:
            string += '#,'
            return string
        else:
            string += node.val + ','

        string = ser(node.left, string)
        string = ser(node.right, string)
        return string
    result = ser(root, '')
    return result

print('serialize')
print(serialize(root))

def deserialize(data):
    queue = data.strip(',').split(',')

    def des(q):
        val = q.pop(0)
        if val == '#':
            return None
        node = Node(val)
        node.left = des(q)
        node.right = des(q)

        return node
    return des(queue)

deserialized = deserialize(serialize(root))
print(serialize(deserialized))
# git test
