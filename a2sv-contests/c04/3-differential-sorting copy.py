tCount = int(input())
for x in range(tCount):
    dataSize = int(input())
    data = [int(i) for i in input().split(' ')]
    ops = []
    # Splitting input into int array

    if data[-2] > data[-1]:
        print(-1)
        continue
    if sorted(data) == data:
        print(0)
        continue

    for i in range(dataSize-1):
        if (data[i] > data[i+1]):
            rightSide = data[i+1:dataSize-1]
            sm = rightSide.index(min(rightSide)) + i+1
            biggest = data[sm+1:].index(max(data[sm+1:])) + sm + 1
            data[i] = data[sm]-data[biggest]
            if (data[i] > data[i+1]):
                print(-1)
                break
            else:
                ops.append(f"{i+1} {sm+1} {biggest+1}")
                # print(f"{i} {sm} {biggest}")
    print(len(ops))
    for op in ops:
        print(op)
    
