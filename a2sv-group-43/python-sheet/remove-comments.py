class Solution:
    commentMode = None

    def removeCommentFromLine(self, source:str) -> str:
        source = list(source)
        # print(f'source - {source}')
        pointer = 0
        cleanLine = []
        while pointer < len(source):
            if (self.commentMode == 'sl'):
                pointer += 1
                pass
            elif (self.commentMode == 'ml'):
                if(pointer < len(source)-1 and source[pointer] == '*' and source[pointer+1] == '/'):
                    self.commentMode = None
                    pointer += 2
                    pass
                else:
                    pointer += 1
                    pass
            else:
                if source[pointer] != "/":
                    cleanLine.append(source[pointer])
                    pointer += 1
                    pass
                elif (pointer < len(source)-1 and source[pointer+1] == "/"):
                    self.commentMode = "sl"
                    pointer += 2
                elif (pointer < len(source)-1 and source[pointer+1] == "*"):
                    self.commentMode = "ml"
                    pointer +=2 
                else:
                    cleanLine.append(source[pointer])
                    pointer += 1
        if (self.commentMode == 'sl'):
            self.commentMode = None
        return ''.join(cleanLine)



    def removeComments(self, source: list[str]) -> list[str]:
        finalAnswer = []
        cache = []
        for line in source:
            current = self.removeCommentFromLine(line)
            if (current != ''):
                if (self.commentMode == "ml"):
                    cache.append(current)
                else:
                    if (set(''.join(cache)) == {' '}):
                        finalAnswer.append(''.join(cache))
                        finalAnswer.append(current)
                        cache = []
                    else:
                        finalAnswer.append((''.join(cache)) + current)
                        cache = []
        return finalAnswer