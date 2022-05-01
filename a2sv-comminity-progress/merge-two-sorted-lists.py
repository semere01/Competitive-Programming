# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
    def mergeTwoLists(self, list1,list2): 
        pointer1 = list1
        pointer2 = list2
        newListHead = ListNode()
        newPointer = newListHead

        while (pointer1 and pointer2):
            if pointer2.val >= pointer1.val:
                newPointer.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
            else:
                newPointer.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
            newPointer = newPointer.next
        
        while pointer1:
            newPointer.next = ListNode(pointer1.val)
            newPointer = newPointer.next
            pointer1 = pointer1.next
        
        while pointer2:
            newPointer.next = ListNode(pointer2.val)
            newPointer = newPointer.next
            pointer2 = pointer2.next

        return newListHead.next




