class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        queens_that_can_attack = []
        chess_range = range(0,8)

        for above in range(king[0]-1, -1, -1):
            if ([above, king[1]]) in queens:
                if [above, king[1]] in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([above, king[1]])
                    break
        
        for below in range(king[0]+1, 8):
            if ([below, king[1]]) in queens:
                if ([below, king[1]]) in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([below, king[1]])
                    break
        
        for left in range(king[1], -1, -1):
            if ([king[0], left]) in queens:
                if ([king[0], left]) in queens_that_can_attack:
                    pass
                else: 
                    queens_that_can_attack.append([king[0], left])
                    break
        
        for right in range(king[1], 8):
            if ([king[0], right]) in queens:
                if ([king[0], right]) in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([king[0], right])
                    break

        top_right_x = king[0]+1
        top_right_y = king[1]-1

        while top_right_x in chess_range and top_right_y in chess_range:
            if [top_right_x,top_right_y] in queens:
                if [top_right_x,top_right_y] in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([top_right_x,top_right_y])
                    break
            top_right_x += 1
            top_right_y -= 1
        
        top_left_x = king[0]-1
        top_left_y = king[1]-1
        while top_left_x in chess_range and top_left_y in chess_range:
            if [top_left_x, top_left_y] in queens:
                if [top_left_x, top_left_y] in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([top_left_x, top_left_y])
                    break
            top_left_x -= 1
            top_left_y -= 1
        
        bottom_left_x = king[0] - 1
        bottom_left_y = king[1] + 1
        
        while bottom_left_x in chess_range and bottom_left_y in chess_range:
            if [bottom_left_x, bottom_left_y] in queens:
                if [bottom_left_x, bottom_left_y] in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([bottom_left_x, bottom_left_y])
                    break
            bottom_left_x -= 1
            bottom_left_y += 1
        
        bottom_right_x = king[0]+1
        bottom_right_y = king[1]+1
        
        while bottom_right_x in chess_range and bottom_right_y in chess_range:
            if [bottom_right_x, bottom_right_y] in queens:
                if [bottom_right_x, bottom_right_y] in queens_that_can_attack:
                    pass
                else:
                    queens_that_can_attack.append([bottom_right_x, bottom_right_y])
                    break
            bottom_right_x += 1
            bottom_right_y += 1
        
        return queens_that_can_attack
            
            
print(Solution().queensAttacktheKing([[0,1],[6,4],[4,7],[0,0],[3,3],[7,7],[2,1],[1,6],[0,4],[4,3],[2,4],[3,7],[3,4],[1,1]], [7,2]))