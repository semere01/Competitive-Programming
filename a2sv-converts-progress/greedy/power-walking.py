testCases = int(input())
for test in range(testCases):
    n, currentRam = [int(i) for i in input().split(" ")]
    requirement = [int(i) for i in input().split(" ")]
    additional = [int(i) for i in input().split(" ")]

    sortedZip = [x for x in sorted(zip(requirement, additional))]
    for r, a in sortedZip:
        if r <= currentRam:
            currentRam += a
        else:
            break
    print(currentRam)
