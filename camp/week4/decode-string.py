class Solution:
    def decodeString(self, s: str, start=0) -> str:
        self.start = start
        result = []
        number_str = []
        
        while self.start < len(s) and s[self.start] != ']':
            if s[self.start].isalpha():
                result.append(s[self.start])
            elif s[self.start].isdigit():
                number_str.append(s[self.start])
            else:
                brackets_str = self.decodeString(s, self.start + 1)
                number = int(''.join(number_str))
                result.append(number * brackets_str)
                number_str = []
            self.start += 1
        
        return ''.join(result)
