# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def swapPairs(self, head):
        if not head: return
        if not head.next: return head
        

        temp = None
        nextPair = head
        finalHead = head.next
        current = head
        while nextPair and nextPair.next:
            current = nextPair
            nextNode = current.next
            nextPair = current.next.next
            nextNode.next = current
            if nextPair and nextPair.next: current.next = nextPair.next
            elif nextPair: current.next = nextPair
            else: current.next = None
                
        
        return finalHead
        

        

        