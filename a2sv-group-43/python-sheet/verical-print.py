class Solution:
    def printVertically(self, s: str) -> list[str]:
        input_split = s.split(" ")
        biggest = len(max(input_split, key=len))
        l = [list((i.ljust(biggest))) for i in input_split]
        words = []
        for i in range(biggest):
            newWord = []
            for word in l:
                newWord.append(word[i])
            words.append((''.join(newWord)).rstrip())
        return words


print(Solution().printVertically("HOW ARE YOU"))
