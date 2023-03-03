# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 0,1,2,3,4,5,6,7
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
        return maxSum
            