from leetcode_imports import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result_head = ListNode(0)
    cur = result_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry

        carry = sum // 10
        cur.next = ListNode(sum % 10)
        cur = cur.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        current.next = ListNode(val=1)

    return result_head.next
