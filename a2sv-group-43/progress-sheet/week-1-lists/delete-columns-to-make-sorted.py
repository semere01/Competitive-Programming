class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deleted_columns_count = 0
        for col_num in range(len(strs[0])):
            sorted_col = True
            for row_num in range(len(strs)-1):
                if ord(strs[row_num][col_num]) > ord(strs[row_num+1][col_num]):
                    sorted_col = False
                    break
            if (not sorted_col):
                deleted_columns_count += 1

        return deleted_columns_count
