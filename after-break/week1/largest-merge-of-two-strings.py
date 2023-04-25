class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        q1 = deque(word1)
        q2 = deque(word2)
        r = []
        def check(q1, q2):
            nonlocal r
            if not q1:
                r += q2
                return
            if not q2:
                r += q1
                return
            if q1 >= q2:
                r.append(q1.popleft())
            else:
                r.append(q2.popleft())
            check(q1, q2)
        check(q1, q2)
        return ''.join(r)