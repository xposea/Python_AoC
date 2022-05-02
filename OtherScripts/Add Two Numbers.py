from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addNode(self, val, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            head = ListNode(val, None)
            return head
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = ListNode(val, None)
        return ptr.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        head = Optional[ListNode]
        track = False
        while curr1 is not None or curr2 is not None:
            val = 0
            if track is True:
                val += 1
                track = False
            if curr1 is not None:
                val += curr1.val
            if curr2 is not None:
                val += curr2.val
            if val >= 10:
                track = True
                val -= 10
            Solution.addNode(self, val, head)
        return head
