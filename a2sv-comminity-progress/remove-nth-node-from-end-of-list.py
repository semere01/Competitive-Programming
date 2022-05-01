class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def removeNthFromEnd(self, head, n):
        print("n: ", n)
        if not head.next: return 
        pointer = head
        cache = [None] * (n+1)
        while pointer:
            cache.pop(0)
            cache.append(pointer)
            pointer = pointer.next
                
        print(f"len(cache)  = {len(cache)}")
        if (head==cache[-1*n]): return head.next
        elif len(cache) == 2: cache[0].next = None
        else: cache[0].next = cache[2]
        return head

