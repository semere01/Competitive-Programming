class RecentCounter:
    def __init__(self):
        self.data = []
        self.p0 = None
    def ping(self, t: int) -> int:
        self.data.append(t)
        if self.p0 == None:
            self.p0 = 0
        while self.data[self.p0] < (self.data[-1] - 3000):
            self.p0 += 1
        return len(self.data) - self.p0
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)