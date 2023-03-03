class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        for i in range(m-1):
            prev = curr
            curr = curr.next
        start = prev
        end = curr
        for i in range(n-m+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        if start:
            start.next = prev
        else:
            head = prev
        end.next = curr
        return head
