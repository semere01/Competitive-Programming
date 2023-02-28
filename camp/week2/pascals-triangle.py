class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if (rowIndex) == 0: return [1]
        prevRow = self.getRow(rowIndex - 1)
        newRow = [1]
        for n in range(len(prevRow)-1):
            newRow.append(prevRow[n] + prevRow[n+1])
        newRow.append(1)
        return newRow
