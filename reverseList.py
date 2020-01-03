class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        tail = head.next
        newHead = self.reverseList(head.next)
        tail.next, head.next = head, None
        return newHead

head = None
lastNode = None
for i in range(1, 6):
    node = ListNode(i)
    if not head:
        head = node
    if lastNode:
        lastNode.next = node
    lastNode = node

def printList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

printList(head)
solution = Solution()
head = solution.reverseList(head)
print("after reverse:")
printList(head)