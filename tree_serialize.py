"""
Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node, array):
    if node == None:
        return
    array.append('{')
    array.append(node.val)
    array.append(',')
    serialize(node.left, array)
    array.append(',')
    serialize(node.right, array)
    array.append('}')

array = []
serialize(node, array)
string = ''.join(array)
print(string)

# input: {root,{left,{left.left,,},},{right,,}}
# not done yet
def deserialize(input):
    controller = []
    values = []
    for char in input:
        if char == '{':
            controller.append(char)
        elif char == '}':
            value = ''
            while len(values) > 0 and values[-1] != '{':
                value += values.pop()
            print(value)
        else:
            values.append(char)

deserialize(string)
