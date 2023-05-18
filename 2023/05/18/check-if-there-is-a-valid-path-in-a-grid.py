from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]
                if val == 1:
                    grid[r][c] = [0,1,0,1]
                elif val == 2:
                    grid[r][c] =  [1,0,1,0]
                elif val == 3:
                    grid[r][c] =  [0,0,1,1]
                elif val == 4:
                    grid[r][c] =  [0,1,1,0]
                elif val == 5:
                    grid[r][c] =  [1,0,0,1]
                elif val == 6:
                    grid[r][c] =  [1,1,0,0]
        
        grid[0][0][0] = 0
        grid[0][0][3] = 0
        val = False
        for i in range(4):
            el = grid[0][0][i]
            if el:
                val = (val or self.hasAValidPath(grid))
                grid[0][0][i] = 0
                if 1 not in grid[0][0]:
                    break
        
        return val

        

    def hasAValidPath(self, grid: List[List[int]]) -> bool:

        opposites = [2, 3, 0, 1]
        location = [0,0]
        current_value:list = grid[location[0]][location[1]]
        while True:
            if (location == [len(grid)-1, len(grid[0])-1]):
                return True
            next_dir = current_value.index(1)
            next_cell = None
            if (next_dir == 0):
                next_cell = [location[0]-1, location[1]]
            elif (next_dir == 1):
                next_cell = [location[0], location[1]+1]
            elif (next_dir == 2):
                next_cell = [location[0]+1, location[1]]
            elif (next_dir == 3):
                next_cell = [location[0], location[1]-1]
            
            if ( next_cell[0] < 0 or next_cell[0] >= len(grid) or next_cell[1] < 0 or next_cell[1] >= len(grid[0])   or  not grid[next_cell[0]][next_cell[1]][opposites[next_dir]]):
                return False
            grid[next_cell[0]][next_cell[1]][opposites[next_dir]] = False
            location = next_cell
            current_value:list = grid[location[0]][location[1]]
