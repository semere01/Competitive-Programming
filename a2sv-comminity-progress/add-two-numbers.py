# Definition for singly-linked list.
from typing import List, final
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1, l2): 
        carry = 0
        head = None
        latest = None
        while (l1 or l2):
            if not l1: l1 = ListNode()
            if not l2: l2 = ListNode()
            currentSum = int(l1.val) + int(l2.val) + int(carry)
            l1 = l1.next
            l2 = l2.next
            if len(str(currentSum)) > 1:
                carry = '1'
            else:
                carry = '0' 

            if not head:
                head = ListNode(str(currentSum)[-1])
                latest = head
            elif not latest:
                head.next = ListNode(str(currentSum)[-1])
                latest = head.next
            else:
                latest.next = ListNode(str(currentSum)[-1])
                latest = latest.next
        if (int(carry) == 1): latest.next = ListNode(str(carry))
        return head
    
