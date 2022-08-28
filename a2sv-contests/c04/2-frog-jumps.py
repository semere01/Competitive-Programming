tCount = int(input())

for t in range(tCount):
    path = list(input())
    largestLCount = 0
    currentLCount = 0
    if "R" not in path:
        print(len(path)+1)
        continue
    for letter in path:
        if letter == "L":
            currentLCount+=1
        if letter == "R":
            if currentLCount > largestLCount:
                largestLCount = currentLCount
            currentLCount = 0
    finalLeap = path[::-1].index("R")+1
    initialLeap = path.index("R")+1
    print(max([finalLeap, initialLeap, largestLCount+1]))

