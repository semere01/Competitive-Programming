tCount = int(input())
for x in range(tCount):
    dataSize = int(input())
    data = [int(i) for i in input().split(' ')]

    if data[-2] > data[-1]:
        print(-1)
    elif sorted(data) == data:
        print(0)
    elif data[-1] >= 0:
        ops = [f"{i+1} {dataSize-1} {dataSize}" for i in range(dataSize-2)]
        print(len(ops))
        for op in ops:
            print(op)
    else: 
        print(-1)

    # for i in range(dataSize-2):
    #     if data[i] > data[i+1]:
    #         for j in range(i+1, dataSize-1):
    #             shouldBreak = False
    #             for k in range(j+1, dataSize):
    #                 if data[j]-data[k] <= data[i+1]:
    #                     data[i] = data[j] - data[k]
    #                     ops.append(f"{i+1} {j+1} {k+1}")
    #                     shouldBreak = True
    #                     break
    #             if shouldBreak: break
    #     if data[i] > data[i+1]:
    #         print(-1)
    #         break

    # for i in range(dataSize-1):
    #     if (data[i] > data[i+1]):
    #         sm = i+1
    #         ex = False
    #         while (True):
    #             if (sm >= dataSize-2):
    #                 ex = True
    #                 break
    #             biggest = data[sm+1:].index(max(data[sm+1:])) + sm + 1
    #             test = data[sm] - data[biggest]
    #             if test <= data[i+1]:
    #                 data[i] = test
    #                 ops.append(f"{i+1} {sm+1} {biggest+1}")
    #                 break
    #             else:
    #                 sm+=1
    #         if ex:
    #             break

        # rightSide = data[i+1:dataSize-1]
        # sm = rightSide.index(min(rightSide)) + i+1
        # biggest = data[sm+1:].index(max(data[sm+1:])) + sm + 1
        # data[i] = data[sm]-data[biggest]
        # if (data[i] > data[i+1]):
        #     print(-1)
        #     break
        # else:
        #     ops.append(f"{i+1} {sm+1} {biggest+1}")
        # print(f"{i} {sm} {biggest}")
