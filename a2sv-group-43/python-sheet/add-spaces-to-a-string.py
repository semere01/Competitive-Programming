class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s = list(s)
        data = [''.join(s[:spaces[0]])]

        for i in range(1, len(spaces)):
            temp = s[spaces[i-1]: spaces[i]]
            data.append(''.join(temp))
        data.append(''.join(s[spaces[-1]:]))

        return " ".join(data)


print(Solution().addSpaces("p", [0]))
