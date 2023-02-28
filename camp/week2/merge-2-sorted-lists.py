# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def appendNecessary(self, list1, list2):
        if (list1 == None and list2 == None):
            pass
        # If one is none
        elif (list1 == None):
            self.latest.next = ListNode(list2.val)
            self.latest = self.latest.next
            list2 = list2.next
            self.appendNecessary(list1, list2)
        elif (list2 == None):
            self.latest.next = ListNode(list1.val)
            self.latest = self.latest.next
            list1 = list1.next
            self.appendNecessary(list1, list2)
        # Compare Values
        elif (list1.val > list2.val):
            self.latest.next = ListNode(list2.val)
            list2 = list2.next
            self.latest = self.latest.next
            self.appendNecessary(list1, list2)
        else:
            self.latest.next = ListNode(list1.val)
            list1 = list1.next
            self.latest = self.latest.next
            self.appendNecessary(list1, list2)
        

    
    def mergeTwoLists(self, list1, list2):
        self.head = ListNode()
        self.latest = self.head
        self.appendNecessary(list1, list2)
        return self.head.next

        # self.head.next
        # mergedList = head
        # head.next = findSmaller(list1, list2)

        

        # while(list1 and list2):
        #     if (list1.val > list2.val):
        #         mergedList.next = ListNode(list2.val)
        #         mergedList = mergedList.next
        #         list2 = list2.next
        #     else:
        #         mergedList.next = ListNode(list1.val)
        #         mergedList = mergedList.next
        #         list1 = list1.next
        
        # while (list1):
        #     mergedList.next = ListNode(list1.val)
        #     mergedList = mergedList.next
        #     list1 = list1.next
        # while (list2):
        #     mergedList.next = ListNode(list2.val)
        #     mergedList = mergedList.next
        #     list2 = list2.next
        

l1 = ListNode(1, ListNode(2, ListNode(4)))

l2 = ListNode(1, ListNode(3, ListNode(4)))

ans = (Solution().mergeTwoLists(l1, l2))

while(ans):
    print(ans.val)
    ans = ans.next

        

