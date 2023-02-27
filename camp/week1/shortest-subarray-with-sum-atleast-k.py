class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        
        min_len = float('inf')
        deque = collections.deque()
        
        for i in range(n + 1):
            while deque and prefix_sum[i] - prefix_sum[deque[0]] >= K:
                j = deque.popleft()
                min_len = min(min_len, i - j)
            
            while deque and prefix_sum[i] <= prefix_sum[deque[-1]]:
                deque.pop()
            
            deque.append(i)
        
        return min_len if min_len != float('inf') else -1
