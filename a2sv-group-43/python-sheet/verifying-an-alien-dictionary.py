class Solution:

    # def compareWord(self, w1:str, w2: str, order:str):
    #     p = 0

    #     while (p < len(w1) and p < len(w2)):
    #         if w1[p] > w2[p]:
    #             return w1
    #         elif w1[p]<w2[p]:
    #             return w2
    #         else:
    #             p += 1
    #     if (p < len(w2)):
    #         return 


    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order = list(order)
        normal_list = []
        for word in words:
            normal_word = []
            for letter in word:
                normal_word.append(chr(ord('a') + order.index(letter)))
            normal_list.append(''.join(normal_word))
        sorted_normal_list = sorted(normal_list)
        return (sorted_normal_list == normal_list)

