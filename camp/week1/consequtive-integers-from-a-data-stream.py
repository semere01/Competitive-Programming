class DataStream:

    def __init__(self, value: int, k: int):
        self.key = value
        self.k = k
        self.streak = 0
        

    def consec(self, num: int) -> bool:
        if (num == self.key):
            self.streak += 1
        else:
            self.streak = 0
        
        if (self.streak < self.k):
            print("self.streak")
            print(self.streak)
            print("self.k")
            print(self.k)
        
        return self.streak >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)