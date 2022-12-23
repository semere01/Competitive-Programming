class Solution:
    def freqAlphabets(self, s: str) -> str:
        pointer = len(s) - 1
        response = []
        while pointer >= 0:  # n
            letter = s[pointer]
            if (letter == "#"):
                letter = int(s[pointer-2] + s[pointer-1]) + ord('j') - 10
                response.append(chr(letter))
                pointer -= 3
            else:
                letter = ord('a') + int(letter) - 1
                response.append(chr(letter))
                pointer -= 1
        return ''.join(response[::-1])
