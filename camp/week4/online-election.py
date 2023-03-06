class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        n = len(persons)
        ranges = []
        map = [0] * 5000
        biggest = 0
        for i in range(n):
            person = persons[i]
            time = times[i]
            map[person] = map[person] + 1
            vote_count = map[person]
            if (vote_count >= biggest):
                biggest = vote_count
                if (len(ranges) == 0 or (len(ranges) and ranges[-1][1] != person)):
                    ranges.append((time, person))

        self.ranges = ranges
        print(f"ranges - {ranges}")

    def q(self, t: int) -> int:
        if self.ranges[-1][0] <= t:
            return self.ranges[-1][1]
        left = 0
        right = len(self.ranges)
        while True:
            i = left + ((right-left) // 2)
            if(t==12):
                print(f"(left, right) - ({left}, {right})")
                print(f"I - {i}")

            if (self.ranges[i][0] == t):
                return self.ranges[i][1]
            if (i+1 < len(self.ranges) and self.ranges[i][0] < t and self.ranges[i+1][0] > t):
                return self.ranges[i][1]
            if (t < self.ranges[i][0]):
                right = i
            else:
                left = i+1
