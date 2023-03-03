class Solution:
    def compress(self, chars): #: List[str]) -> int:
        if chars == None: return
        if len(chars) == 1: return 1

        stoppingPoint = len(chars)
        pointerLocation = 0
        lastVal = chars[0]
        compressedLength = 0
        pointer = None
        currentCount = 0

        while pointerLocation < stoppingPoint:
            pointer = chars[pointerLocation]
            pointerLocation +=1 
            if pointer != lastVal:
                if currentCount == 1:
                    compressedLength += 1
                    chars += lastVal
                else:
                    chars += lastVal + str(currentCount)
                    compressedLength +=(1+len(str(currentCount)))
                currentCount = 1
            else:
                currentCount += 1
            lastVal = pointer

        if currentCount == 1:
            compressedLength += 1
            chars += str(lastVal)
        else:
            compressedLength += (1+len(str(currentCount)))
            chars += ([str(lastVal)] + ([c for c in str(currentCount)]))
        del(chars[:stoppingPoint])
        return compressedLength;
    