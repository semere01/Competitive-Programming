
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Convert to list
        word1 = list(word1)
        word2 = list(word2)

        # Extract Length
        len_w1, len_w2 = len(word1), len(word2)
        p1, p2 = 0, 0
        merged_list = []

        while (p1 < len_w1 and p2 < len_w2):
            merged_list.append(word1[p1])
            merged_list.append(word2[p2])
            p1 += 1
            p2 += 1

        while (p1 < len_w1):
            merged_list.append(word1[p1])
            p1 += 1

        while (p2 < len_w2):
            merged_list.append(word2[p2])
            p2 += 1

        return ''.join(merged_list)
