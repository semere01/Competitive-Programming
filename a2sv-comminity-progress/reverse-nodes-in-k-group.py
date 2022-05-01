class Solution:
    def reverse(self, start, end):
        r = None        
        curr = start        
        while curr!=end:
            prev=curr
            curr = curr.next
            prev.next = r             
            r = prev
        start.next = end
        return r 
    def reverseKGroup(self, head, k):
        dummy=ListNode(-1, head) 
        prev=dummy
        curr = head        
        while curr:
            start = curr
            i = k
            while curr and i: 
                curr=curr.next
                i -= 1
            if not i:                         
                prev.next = self.reverse(start, curr)
                prev = start                           
        return dummy.next
