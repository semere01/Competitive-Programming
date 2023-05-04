class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.maxLength = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.data,  val)
        if (len(self.data) > self.maxLength):
            heapq.heappop(self.data)
        return self.data[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)