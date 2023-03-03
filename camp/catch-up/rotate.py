class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # tail = head.next
        # length = 0
        length = 1
        # length = 0
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            # print(length)
        k = k % length
        if k == 0:
            return head
        new_tail = head
        for _ in range(length - k - 1):
            # print(i)
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
