class Solution:
    def carFleet(self, target, position: list[int], speed: list[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        position = list(position)
        speed = list(speed)
        print(f"position - {position}")
        print(f"speed - {speed}")
        t = []
        fleet_count = 1
        for i in range(len(position)):
            curr_position = position[i]
            curr_speed = speed[i]
            remaining_distance = target - curr_position
            curr_time = remaining_distance // curr_speed 
            t.append(curr_time)
        
        for i in range(len(position)-1, 0, -1):
            if t[i] - t[i-1] < 0:
                fleet_count += 1

        return fleet_count

#         print(f"position - {position}")
#         print(f"speed    - {speed}")


#         while (len(position) >  1):
#             p = 0
#             while (p < len(position) - 1):
#                 curr_position = position[p]
#                 curr_speed = speed[p]
#                 next_position = position[p+1]
#                 next_speed = speed[p+1]

#                 if (curr_position + curr_speed) >= (next_position + next_speed):
#                     position.pop(p)
#                     speed.pop(p)
#                     fleet_count -=1
#                 else:
#                     position[p] = curr_position + curr_speed
#                     if position[p] >= target:
#                         position.pop(p)
#                         speed.pop(p)
#                         fleet_count-=1
#                     else:p += 1
#             if (len(position) and p == len(position)-1):
                
#                 curr_position = position[p]
#                 curr_speed = speed[p]
#                 position[p] = curr_position + curr_speed
#                 if position[p] >= target:
#                     position.pop(p)
#                     speed.pop(p)

#         return fleet_count


print(Solution().carFleet(12, [10, 8, 0,5,3], [2,4,1,1,3]))



