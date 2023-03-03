# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def deleteDuplicates(self, head):
        if not head: return
        currentPointer = head
        while currentPointer and currentPointer.next:
            if currentPointer.val == currentPointer.next.val:
                currentPointer.next = currentPointer.next.next
            else:
                currentPointer = currentPointer.next
        
        return head
        