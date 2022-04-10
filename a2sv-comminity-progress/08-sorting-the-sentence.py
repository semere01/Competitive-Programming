class Solution:
    def sortSentence(self, s: str) -> str:
        sAsList = s.split(" ")
        sAsList.sort(key=lambda x: x[-1])
        sAsList = [word[:-1] for word in sAsList]
        return " ".join(sAsList);

s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))