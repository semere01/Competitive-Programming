class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # n = number of friends
        # k = length of count
        self.game = [i for i in range(n)]
        offset = 0
        while len(self.game) != 1: 
            offset =  ((k + offset) % len(self.game)) - 1
            kicked = self.game.pop((offset % len(self.game)))
            if offset < 0 or offset >= len(self.game): offset = 0
        return (self.game[0]+1)
