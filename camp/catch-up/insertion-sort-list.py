class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        d=ListNode(-1)
        res=d
        for i in l:
            res.next=ListNode(i)
            res=res.next
        return d.next