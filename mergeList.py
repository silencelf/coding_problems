class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        newHead = ListNode(None)
        def merge(l1, l2, current):
            if not l1 or not l2:
                current.next = l1 if l1 else l2
                return
            if l1.val > l2.val:
                l1, l2 = l2, l1
            n = l1.next
            current.next, l1.next = l1, None
            merge(n, l2, current.next)

        merge(l1, l2, newHead)
        return newHead.next

l3 = ListNode(4)
l2 = ListNode(2)
l1 = ListNode(1)
l1.next, l2.next = l2, l3

r3 = ListNode(4)
r2 = ListNode(3)
r1 = ListNode(1)
r1.next, r2.next = r2, r3
s = Solution()
result = s.mergeTwoLists(l1, r1)

while result:
    print(result.val, end=" -> ")
    result = result.next