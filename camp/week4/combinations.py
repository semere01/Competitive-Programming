class Solution:
    def combine(self, n: int, k: int):
        mega = []
        for i in range(1, n+1):
            self.rec(i, [], mega, n, k)
        return mega

    def rec(self, cur_int, curr_ans, mega, n, k):
        curr_ans.append(cur_int)
        if (len(curr_ans) == k):
            mega.append(curr_ans)
            return
        for i in range(cur_int+1, n+1):
            
            self.rec(i, curr_ans.copy(), mega, n, k)
