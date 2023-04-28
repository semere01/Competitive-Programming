from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        keyBag = deque([0])

        visited = set()

        while keyBag:
            key = keyBag.popleft()
            if key not in visited:
                # Visiting the room
                for next_key in rooms[key]:
                    if (next_key not in visited):
                        keyBag.append(next_key)
                visited.add(key)

        return len(visited) == len(rooms)



