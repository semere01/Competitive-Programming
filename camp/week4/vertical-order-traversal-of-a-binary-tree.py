class Solution:
    def verticalTraversal(self, root):
        data = {}
        self.rec_func(root, data, 0,0)

        col_keys = [k[0] for k in sorted(data.items(), key= lambda x: x[0])]
        
        result = []
        for col_index in col_keys:
            curr_col_res = []
            col_rows = data[col_index]
            row_keys = [k[0] for k in sorted(col_rows.items(), key= lambda x: x[0])]
            for row_index in row_keys:
                curr_col_res += sorted(col_rows[row_index])
            
            result.append(curr_col_res)
        return result
    
    def rec_func(self, root, data, row, col):
        if (root == None):
            return
        data[col] = data.get(col, {})
        data[col][row] = data[col].get(row, [])
        data[col][row].append(root.val)
        self.rec_func(root.right, data, row+1, col+1)
        self.rec_func(root.left, data, row+1, col-1)


