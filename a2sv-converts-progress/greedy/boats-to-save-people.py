class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        count = 0
        while len(people) > 1:
            person = people.pop(-1)
            if person + people[0] <= limit:
                people.pop(0)
            count += 1
        if people: count += 1
        return count

