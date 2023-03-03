# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):
        if (not head): return
        pointer1 = head
        pointer2 = head.next
        temp = True
        # pointer3 = None
        if pointer2 == None: return pointer1

        while temp:
            temp = pointer2.next
            pointer2.next = pointer1
            pointer1 = pointer2
            pointer2 = temp
        head.next = None
        return pointer1