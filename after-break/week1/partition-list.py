
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_head = ListNode()
        less = less_than_head
        greater_or_equal_than_head = ListNode()
        greater_or_equal = greater_or_equal_than_head
        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                greater_or_equal.next = ListNode(head.val)
                greater_or_equal = greater_or_equal.next
            head = head.next
        less.next = greater_or_equal_than_head.next
        return less_than_head.next