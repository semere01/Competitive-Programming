# Definition for singly-linked list.
class ListNode:
    def __str__(self):
        return(f"Value: {self.val} | Next Exists: {bool(self.next)}\n")
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self):
        x = self
        while x:
            print(x)
            x = x.next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):
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

i1 = ListNode(1)
i2 = ListNode(2)
i3 = ListNode(3)
i4 = ListNode(4)
i5 = ListNode(5)

i1.next = i2
i2.next = i3
i3.next = i4
i4.next = i5

# i1.printList()
x = Solution().reverseList(i1)
print(x)
x = x.next
print(x)
x = x.next
print(x)
x = x.next
print(x)
x = x.next
print(x)
x = x.next
print(x)
# print(x.next)
# print(x.next)
# print(x.next)
# print(x.next)
