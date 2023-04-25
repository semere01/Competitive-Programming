class Solution:
    def maxLength(self, arr: List[str]) -> int:
        binaries = []
        for item in arr:
            x = 0
            if len(set(item)) != len(item):
                continue
            for c in item:
                x += 1<<ord(c) - ord('a')
            binaries.append(x)
        # [print(bin(x)[2:]) for x in binaries]
        easy_exit = int("1" * 26, base=2)
        @cache
        def longest_s(v, i):
            if i == len(binaries) or v == easy_exit:
                return v
            a = 0
            if v | binaries[i] == v ^ binaries[i]:
                a = longest_s(v | binaries[i], i+1)
            b = longest_s(v, i+1)
            a_c = bin(a).count("1")
            b_c = bin(b).count("1")
            return a if a_c > b_c else b
        out = longest_s(0, 0)

        return bin(out).count("1") 