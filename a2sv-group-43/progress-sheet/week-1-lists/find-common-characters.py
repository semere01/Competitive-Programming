class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count_list = self.getCountMap(words[0])
        for index in range(1, len(words)):
            word = words[index]
            current_map = self.getCountMap(word)
            for i in range(len(current_map)):
                if current_map[i] < count_list[i]:
                    count_list[i] = current_map[i]

        common_letters = []
        for index in range(len(count_list)):
            count = count_list[index]
            for i in range(count):
                common_letters.append(chr(index+97))

        return common_letters

    def getCountMap(self, word: str) -> list[int]:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - 97] += 1

        return count


print(Solution().commonChars(["cool", "lock", "cook"]))
