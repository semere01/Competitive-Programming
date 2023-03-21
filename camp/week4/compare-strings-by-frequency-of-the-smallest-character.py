class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        n_w = len(words)
        n_q = len(queries)
        w_counts = [self.f(x) for x in words]
        w_counts.sort()
        q_counts = [self.f(x) for x in queries]

        return_list = []
        for q_count in q_counts:
            left = 0
            right = len(w_counts)
            while(left +1 < right):
                curr =  ((right+left)//2)
                w_count = w_counts[curr]
                if (w_count > q_count):
                    right = curr
                if (w_count <= q_count):
                    left = curr
            return_list.append(len(w_counts)-left)
        return return_list

    def f(self, s):
        s = list(s)
        data = [0] * 26

        for letter in s:
            data[ord(letter) - ord('a')] += 1

        for d in data:
            if d != 0:
                return d

data = [
    # ["cbd"],
    # ["zaaaz"],
    ["bbb", "cc"],
    ["a", "aa", "aaa", "aaaa"]
]

for i in range(0, len(data), 2):
    # print((data[i], data[i+1]))
    print(Solution().numSmallerByFrequency(data[i], data[i+1]))

