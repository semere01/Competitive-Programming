
class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def deleteDuplicates(self, head):
        if not head:
            return
        if not head.next:
            return head
        # remove duplicates from head
        while head.next and head.val == head.next.val:
            temp = head.next
            while temp and temp.val == head.val:
                temp = temp.next
            if not temp:
                return
            head = temp


        # while head.next and head.val == head.next.val:
            # head = head.next.next
        originalHead = head
        p1 = head
        while p1.next and p1.next.next:
            p2 = p1.next
            if p2.val == p2.next.val:
                while p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                p1.next = p2.next
                continue
            p1 = p2
        return originalHead
        
        