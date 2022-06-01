# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getCount(self, head):
        counter = 1
        current = head
        while (current.next != None):
            current = current.next
            counter += 1

    # def pairSum(self, head: Optional[ListNode]) -> int:
    def pairSum(self, head):
        if head == None: return
        count = 1
        last = head
        while (last.next != None):
            last = last.next
            count += 1
        
        counter = 0
        firstHalf = head
        secondHalf = firstHalf
        while (counter < count/2):
            nextPointer = secondHalf.next # caching
            secondHalf.next = firstHalf
            firstHalf = secondHalf
            secondHalf = nextPointer
            counter+=1
        head.next = None
        
        maxSum = 0
        while (firstHalf != None):
            currentSum = firstHalf.val + secondHalf.val
            if (maxSum < currentSum):
                maxSum = currentSum
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

s = Solution()
l3 = ListNode(100)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
l0 = ListNode(0, l1)
s.pairSum(l0)

