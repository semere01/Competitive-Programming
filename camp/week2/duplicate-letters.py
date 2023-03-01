class Solution:
    def removeDuplicateLetters(self, string: str) -> str:
        final = []
        string = list(string)

        for index in range(len(string)):
            letter = string[index]

            if final == []:
                final.append(letter)
            elif letter in final:
                continue
            elif final[-1]<letter:
                final.append(letter)
            elif final [-1] > letter:
                if final[-1] in string[index:]:
                    while len(final) and final[-1] in string[index:] and final[-1] > letter:
                        final.pop()
                final.append(letter)
        
        return ''.join(final)
                
